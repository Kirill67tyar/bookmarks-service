"""bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('images/', include('images.urls', namespace='images')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# по какой-то причине функция static подходит только для локальных серверов
# ее крайне нежелательно использовать в продакшене (а может и не получится)

# bookmarks_admin
# bookmarks_admin@yandex.ru
# mysite.com:8000

# --------------------------facebook application:
# http://mysite.com:8000/
# bookmarks
# ID приложения: 503791577470729
# https://developers.facebook.com/apps/503791577470729/settings/basic/

# http://mysite.com:8000/social-auth/complete/facebook/
# https://mysite.com:8000/social-auth/complete/facebook/


# --------------------------google application:
# nameappication - MyProject61365


# for sslserver (HTTPS):
# python manage.py runsslserver
# https://github.com/Kirill67tyar/django-sslserver

# https://83b42dc00ec9.ngrok.io/accounts/login/

