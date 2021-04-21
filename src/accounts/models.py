from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User as U
User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Юзер')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='День рождения')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name='Фото')
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        
    def __str__(self):
        return f'Profile for user {self.user.username}'




kwargs1 = {
    'to': User,
    'on_delete': models.CASCADE,
    'related_name': 'rel_from_set',
    'verbose_name': 'От юзера',
}
kwargs2 = kwargs1.copy()
kwargs2['related_name'] = 'rel_to_set'
kwargs2['verbose_name'] = 'К юзеру'



# В данном случае мы делаем промежуточную модель для ManyToMany
# Промежуточная модель необходима, когда нужно сохранить дополнительную
# информацию об отношениях (timestamp к примеру)
# но такая модель будет иметь и недостатки, будут отсутствовать
# встроенные методы ManyToMany методы add(), create(), remove()
# теперь нужно будет явно добавлять и удалять объекты промежутоной модели
# А вообще proxy таблица от django подходит в большинстве случаев
# определяется промежуточная модел примерно так:
"""
    models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
"""
# Вместо self может быть нужная модель
class Contact(models.Model):

    user_from = models.ForeignKey(**kwargs1)
    user_to = models.ForeignKey(**kwargs2)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано', db_index=True)

    def __str__(self):
        return f'{self.user_from} follow {self.user_to}'


# здесь мы прибавляем к нашей базовой модели User новое поле (аттрибут)
# сначала название поля, потом его значение.
# Лучше так динамически не прибавлять аттрибуты (поля)
# без видимых на то причин

# symmetrical=False здесь потому, привязываем поле manytomany на туже самую модель
# django воспроизводит семметриные отношения (дублирует запись?)
# при ссылке на self.
# symmetrical=False делает их несимметриными
U.add_to_class(
    'following',
    models.ManyToManyField(
        'self',
        through=Contact,
        related_name='followers',
        symmetrical=False))


# аргументы add_to_class - cls, name, value

# Алгоритм создания своей промежуточной модели:
# 1) Создаем свою модель с двумя ForeignKey на нужные модели
# 2) Создаем в одной из связанных моделей поле ManyToManyField
# 3) Указываем нашу промежуточную модель в именованном аргументе through= в ManyToMany

