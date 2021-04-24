from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

from images.utils import my_custom_slugify

User = settings.AUTH_USER_MODEL

class Image(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images_created', verbose_name='Владелец')
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, blank=True, verbose_name='Слаг')
    url = models.URLField(verbose_name='Ссылка на оригинальную картинку')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Создана')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создана')
    users_like = models.ManyToManyField(User, related_name='images_liked', verbose_name='Юзеры поставили лайк')
    total_likes = models.PositiveIntegerField(db_index=True, default=0)
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ('created',)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(my_custom_slugify(str(self.title)))
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):

        kwargs = {
            'id': self.pk,
            'slug': self.slug,
        }
        return reverse('images:detail', kwargs=kwargs)

