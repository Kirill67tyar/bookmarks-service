from django.contrib.auth import views # обработики аутентификации из коробки django
from django.contrib.auth.backends import ModelBackend
from django.middleware.security import SecurityMiddleware
from social_core.backends.facebook import FacebookOAuth2
from social_core.backends.twitter import TwitterOAuth
from social_core.backends.google import GoogleOAuth2
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models




# Сделать в будущем авторизацию через telegram, vk, google
# from social_core.backends.






'django.contrib.auth.backends.ModelBackend'
'social_core.backends.facebook.FacebookOAuth2'
'social_core.backends.twitter.TwitterOAuth'
'social_core.backends.google.GoogleOAuth2'

views = views
'django.middleware.security.SecurityMiddleware'


"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""

#                                           social_django
# pip install social-auth-app-... (django)
# path('social-auth/', include('social_django.urls', namespace='social')),

# Ссылка для template.html
# {% url 'social:begin' 'facebook' %}