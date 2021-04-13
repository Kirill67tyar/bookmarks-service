from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

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