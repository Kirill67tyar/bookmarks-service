from django.forms import Form, ModelForm, HiddenInput, ValidationError,  URLField
from django.core.files.base import ContentFile
from django.utils.text import slugify

from urllib import request
import requests

from images.models import Image
from images.utils import my_custom_slugify

def check_etxtension(url):
    valid_extensions = ['jpg', 'jpeg', ]
    image_extension = url.rsplit('.', 1)[1].lower()
    # image_format = url.split('.')[-1].lower()
    if image_extension not in valid_extensions:
        raise ValidationError('The given url does not match valid image extensions (jpg, jpeg)')
    return url

def get_extension(url):
    """

    :param url:
    :return extension (формат .jpg/jpeg/png):
    """
    return url.rsplit('.', 1)[1].lower()

class ImageCreateModelForm(ModelForm):

    # url = URLField(widget=HiddenInput, validators=[check_etxtension,])
    # url = URLField(widget=HiddenInput, required=False)

    class Meta:
        model = Image
        fields = ('title', 'url', 'description',)
        widgets = {
            'url': HiddenInput,
        }
        # labels = {}

    def clean_url(self):
        url = self.cleaned_data.get('url')
        valid_extensions = ['jpg', 'jpeg',]
        # get_extension - моя кастомная функция, см. выше
        image_extension = get_extension(url=url)
        # image_extension = url.split('.')[-1].lower()
        if image_extension not in valid_extensions:
            raise ValidationError('The given url does not match valid image extensions (jpg, jpeg)')
        return url



    def save(self, force_insert=False, force_update=False, commit=True):

        """
        :param force_insert:
        :param force_update:
        :param commit: True/False
        :return:
        Этот save() делает get запрос по url из формы
        и сохраняет картинку полученную картинку
        """
        # получаем несохраненный экземпляр модели Image
        image_instance = super(ImageCreateModelForm, self).save(commit=False)
        url = self.cleaned_data['url']

        # slug здесь нужен для image_name
        slug = slugify(my_custom_slugify(image_instance.title))
        image_name = f'{slug}.{get_extension(url)}'

        # делаем get запрос по адресу картинки или с помощью requests или urllib.request
        response = requests.get(url=url)
        # response = request.urlopen(url=url) # запасной вариант так сказать

        # здесь мы используем save() от поля image экземпляра класса ImageField
        # а не от модели Image или ModelForm
        # он нужен специально чтобы сохранять из кода см. на этот метод в том классе
        # ContentFile(response.read())
        image_instance.image.save(name=image_name, content=ContentFile(response.content), save=False)
        # А вот зачем нужен ContentFile - я хз, но догадываюсь

        if commit:
            image_instance.save()

        return image_instance
