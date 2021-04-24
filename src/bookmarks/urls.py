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
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('images/', include('images.urls', namespace='images')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)),)
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



# -----------------Что нужно делать, чтобы bookmarklet работал:

# 1) заходишь в прогу ngok (C:\Users\User\Desktop\Job\usefull_progs\ngrok-stable-windows-386)
# 2) набираешь в консоли ngrok http 8000
# 3) полуаешь нечтно такое:
"""
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    http://83b42dc00ec9.ngrok.io -> http://localhost:8000
    Forwarding                    https://83b42dc00ec9.ngrok.io -> http://localhost:8000
"""
# 4) меняешь старый хост на новый полученный, в 3 местах в проекте:
# - settings.py (ALLOWED_HOSTS)
# - images/templates/bookmarklet_launcher.js
# - static/js/bookmarklet.js
# 5) ...
# 6) PROFIT!!!

# https://83b42dc00ec9.ngrok.io/accounts/login/
# https://438e2043a0d4.ngrok.io/accounts/login/
# https://f329b1815187.ngrok.io/accounts/login/

