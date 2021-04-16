from django.contrib.auth import views # обработики аутентификации из коробки django
from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
from django.middleware.security import SecurityMiddleware
from social_core.backends.facebook import FacebookOAuth2
from social_core.backends.twitter import TwitterOAuth
from social_core.backends.google import GoogleOAuth2
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models




# Сделать в будущем авторизацию через telegram, vk
# from social_core.backends.




# HttpRequest = HttpRequest

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

#                                    python-social-auth  (social_django)

# https://python-social-auth.readthedocs.io/en/latest/
# https://python-social-auth.readthedocs.io/en/latest/configuration/settings.html
# Очень крутое приложение. Позволяет авторизироваться через соц сети и не только
# Есть возможность авторизации через вк, ок, mail.ru, google и т.д.
# Есть даже через steam и discord. Проверь варианты:
# from social_core.backends.


# 1) pip install social-auth-app-... (django)
# 2) в INSTALLED_APPS добавить 'social_django'
# 3) создать таблицы в бд (python manage.py migrate)
# 4) добавляешь в корневой urls.py path('social-auth/', include('social_django.urls', namespace='social')),
# 5) В settings должен быть указан обязательно LOGIN_REDIRECT_URL = 'accounts:dashboard' (свой app_name и pathname)
# туда куда будет релиректиться при успешной аутентификации
# 6) В settings должен быть указан обязательно AUTHENTICATION_BACKENDS
# с базовой аутентификацией и дополнительным аутентификациями от python-social-auth, как
# 'social_core.backends.google.GoogleOAuth2'
# 7) Создаешь приложение или бот, или гуглишь что и как нужной соц сети
# 8) по итогу подключаешь SOCIAL_AUTH_FACEBOOK_KEY и SOCIAL_AUTH_FACEBOOK_SECRET (FACEBOOK на другое приложение)
# см. в settings.py


# Ссылка для template.html
# {% url 'social:begin' 'facebook' %}

# Могут быть свои нюансы, так например facebook принимает только HTTPS, а google может и HTTP
# А twitter вообще говнище редкостное.





# Поле, которое ссылается на другую таблицу один к одному и один ко многим
# назывется внешним ключом.

# Индекс баз данных (index_db=True) улучшают производительность
# Имеет смысл добвлять когда поле часто используется для filter(), exclude(), order_by()
# Для полей с unique=True или ForeignKey индексы создаются автоматически
# на SlugField (возможно!) тоже формируется автоматически db_index
# для определения составного индекса можно использовать Meta.index_together (хз что такое)

# Зачем нужен commit=False в save() модельной формы?
# это позволяет создать объект экземпляр модели без непосредственного сохранения его в бд (SQL запроса в бд)
# это как если создать экземпляр модели но не сохранять ее.

# Кстати, request - экземпляр класса HTTPRequest:
# from django.http import HttpRequest




# Как сделать строку словарем (строка с синтаксисом python словаря, не json):
# import ast
# s='{(43, 7): 1, (38, 7): 1}'
# d=dict(ast.literal_eval(s))




"""
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://83b42dc00ec9.ngrok.io -> http://localhost:8000
Forwarding                    https://83b42dc00ec9.ngrok.io -> http://localhost:8000
"""

# заходишь в прогу ngok
# набираешь в консоли ngrok http 8000