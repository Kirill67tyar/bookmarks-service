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
from redis import StrictRedis



# Сделать в будущем авторизацию через telegram, vk
# from social_core.backends.


"""
https://github.com/MSOpenTech/redis/raw/2.6/bin/release/redisbin64.zip
"""

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

# У ManyToMany у менеджера объектов есть три отлиных метода:
# .add() - добаляет связь, и не вызывает ошибку и не дублирует если связь уже есть
# .remove() - удаляет связь, и не вызывает ошибку, если связи нет
# .clear() - удаляет все отношения в промежутоной таблицу
# И не забывай, что при связи ManyToMany мы всегда работаем с одним из объектов модели.

# Зачем нужен commit=False в save() модельной формы?
# это позволяет создать объект экземпляр модели без непосредственного сохранения его в бд (SQL запроса в бд)
# это как если создать экземпляр модели но не сохранять ее.

# Кстати, request - экземпляр класса HTTPRequest:
# from django.http import HttpRequest

# from django.http import JsonResponse
# JsonResponse - сериализует словарь в JSON объект И возвращает HTTP ответ с хэдером type: application/json
# с этим Json'ом в body
# зайди http://127.0.0.1:8000/images/experiment/
# контроллер по этому урлу покажет что делает JsonResponse - преобразует объект python в json объект
# возможно ее можно неплохо использовать в rest API

# Как сделать строку словарем (строка с синтаксисом python словаря, не json):
# import ast
# s='{(43, 7): 1, (38, 7): 1}'
# d=dict(ast.literal_eval(s))






# Что нужно делать, чтобы bookmarklet работал:
# 1) заходишь в прогу ngok (C:\Users\User\Desktop\Job\usefull_progs\ngrok-stable-windows-386)
# 2) набираешь в консоли ngrok http 8000
# 3) полуаешь нечтно такое:
"""
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    http://83b42dc00ec9.ngrok.io -> http://localhost:8000
    Forwarding                    https://83b42dc00ec9.ngrok.io -> http://localhost:8000
"""
# 4) меняешь старый хост на новый полуенный, в 3 местах в документе:
# - settings.py (ALLOWED_HOSTS)
# - images/templates/bookmarklet_launcher.js
# - static/js/bookmarklet.js
# 5) ...
# 6) PROFIT!!!





# и экземпляров класса FileField и ImageField есть огромное кол-во своих методов:
# как то: save(), url() ...
# Это связано со спецификой работы с файлами в django
# Вот все эти методы
"""
chunks
close
closed
delete
encoding
field
file
fileno
flush
height
instance
isatty
multiple_chunks
name
newlines
open
path
read
readable
readinto
readline
readlines
save
seek
seekable
size
storage
tell
truncate
url
width
writable
write
writelines
"""

# ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js

# тэг with в шаблонах - хороший способ избежать многократного выисления
# queryset'ов (делать дополнительные SQL запросы)
# но для него нужен закрывающий тег {% endwith %}
# см. как работает в image/detail.html
# а вообще теги Django обрабатываются на сервере. Именно поэтому иногда можно смешивать
# JS с тегами Django, ведь javascript код выполняется в браузере

# The Document Object Model (DOM) - гугли про это (очень важная тема)

#               select_related
# select_related() - позволяет полуить объекты связнные Один ко Многим, и Один к Одному
# запрос полуится чуть более сложным, но позволит избежать многократного обращения к бд
# для доступа к связанным объектам.
# Вкратце: достает все свзанные объекты из таблицы при связи один ко многим, и один к одному.
# его желательно поаще использовать наряду с values() и values_list()
# select_related('some_field') - добавляет в SQL запрос инструкцию JOIN
# и вклюит поля связанного объекта в инструкцию SELECT
# важно указывать конкретные поля в select_related('some_field', 'some_field__from_another_model')
# потому что иначе select_related достанет все связанные поля модели Один к Одному и Один ко Многим
# этой модели
# отлиный способ использования select_related() (выбрать связанное) смотри в контроллере
# dashboard_view в accounts.views
# Важно помнить! для связи Многие к Одному(обратная от один ко многим) и Многие ко Многим
# select_related - не работает. Для этого есть prefetch_related

# prefetch_related (связанные с предварительной выборкой)- может тоже,
# что и select_related, но может также добавить связи Многие ко многим и Многие к Одному
# но работает prefetch_related совершенно не так как select_related
# prefetch_related - ищет объекты не в базе данных а на уровне python
# используя prefetch_related мы можем обращаться к полям GenericForeignKey и GenericRelation


#                   Денормализация
# Денормализация (англ. denormalization) — намеренное приведение структуры базы данных в состояние,
# не соответствующее критериям нормализации, обычно проводимое с целью ускорения операций чтения
# из базы за счет добавления избыточных данных.
# https://habr.com/ru/post/64524/
# Также гугли что такое нормализация - нормализация и денормализация - это базовые
# понятия для работы с бд
# https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%84%D0%BE%D1%80%D0%BC%D0%B0
# https://ru.wikipedia.org/wiki/%D0%9F%D1%8F%D1%82%D0%B0%D1%8F_%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%84%D0%BE%D1%80%D0%BC%D0%B0#%D0%94%D0%B5%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%B7%D0%B8%D1%86%D0%B8%D1%8F_%D0%B1%D0%B5%D0%B7_%D0%BF%D0%BE%D1%82%D0%B5%D1%80%D1%8C

# Что есть денормализация? Вот у нас есть две модели User и Image
# и связаны они по полю ManyToMany (промежутоная таблица).
# Каждый юзер может лайкнуть сколько угодно картинок. Каждая картинка может быть лайкнута
# сколько угодно раз.
# Как отсортировать QuerySet Image по количеству лайков?
# images = Image.objects.annotate(cnt_likes=Count('users_liked')).order_by('-cnt_likes')
# Такой подход имеет недостаток, так как мы снала делаем запрос количетво лайков
# потом сортируем. В общем полуается довольно затратный запрос.
# А можно просто в Image задать поле PositiveIntegerField и это поле будет отвеать
# за количество лайков. Когда создается новая запись в прокси таблице о том что юзер лайкнул картинку
# просто увеличивать PositiveIntegerField на 1. Короче это поле будет отвеать за
# количество лайков у экземпляра Image.
# Такой процесс и называется денормализацией.



# Каким образом полуить промежуточную модель? очень просто, через аттрибут through
# class Task(Model);
#   tags = ManyToMany(Tag)

# t = Task.objects.first()
# t.tags.through - полуишь промежутоную модель ManyToMany, и даже сможешь работать с ней,
# получать QuerySet


#                               Сигналы
# m2m_changed - это наш сигнал
# декоратор receiver принимает сигналы

# пример использования сигналов - images.signals
# 1) мы регистрируем функцию users_like_changed как наш подписчик с помощью декоратора receiver.
# 2) далее мы подписываемся на сигнал m2m_changed

# сигналы в django расположены по директории django.db.models.signals
# django предоставляет несколько сигналов для моделей:

# Сигналы очень полезны, если нам надо выполнить определенную обработку
# при наступлении определенного события

# грубо говоря функция подписик декоратора receiver будет уведомлена, что
# произошло определенное действие
"""
pre_init = ModelSignal(use_caching=True) - !!видимо!! перед добавлением объекта в модель
post_init = ModelSignal(use_caching=True) - !!видимо!! после добавления объекта в модель

pre_save = ModelSignal(use_caching=True) - перед добавленем объекта в db
post_save = ModelSignal(use_caching=True) - после добавления объекта в db

pre_delete = ModelSignal(use_caching=True) - перед удалением объекта в db
post_delete = ModelSignal(use_caching=True) - перед удаления объекта в db

m2m_changed = ModelSignal(use_caching=True) - если прокси таблица ManyToMany была изменена

pre_migrate = Signal() - !!видимо!! перед миграциями
post_migrate = Signal() - !!видимо!! после миграций
"""
# Внезапно, мы можем писать свои сигналы (сигналы - экземпляры класса ModelSignal)


""" Своими словами: 
сигналы нужны для чтобы выполнялось определенное действие при определенном действии в какой-то асти приложения
пока сложно сказать насколько это нужно, но в книги советуют часто не использовать сигналы
Во всяком случае мы могли бы сделать тоже самое в контроллере"""


#                       apps.py

# При создании приложения! django создает определяет конфигурационный класс
# при создании приложения создается файл apps.py где описан базовый конфигурационный класс
# он унаследован от AppConfig - эти классы позволяют нам хранить методанные приложения
# и предоставляют нам интроспекцию
# https://docs.djangoproject.com/en/3.2/ref/applications/

# Интроспекция (англ. type introspection) в программировании — возможность запросить тип
# и структуру объекта во время выполнения программы.

# метод ready() - вызывается сразу как только заполнен реестр приложения
# любая логика связанная с инициализацией нашего приложения должна быть объяснена в этом методе


""" Своими словами: 
базовый класс композиции приложения в apps.py, заимствованный от AppConfig
класс, который содержит метаданные
очень условно - это можно назвать эдаким аналогом ContentType для модели
Если нужно задать определенные значения при инициализации приложения - нужно использовать этот класс"""


#                   Redis

# хранилище данных, которое хранит данные в формате клю значение
# можно:
# - задать данные SET key value
# - полуить GET key
# - проверить существуют ли дынные EXISTS key
# - удалить DELETE key
# - удалить через n секунд EXPIRE key n    (Где n - колиество секунд ввиде числа)
# - удалить в нужное время EXPIREAT key 00:00:00    (может формат времени пишется по другому)


# по работе Redis в python:
# https://pypi.org/project/redis/
#
# по работе Redis в django:
# https://github.com/jazzband/django-redis

# официальный сайт Redis:
# https://redis.io/

# команды и документация Redis:
# https://redis.io/commands
# https://redis.io/documentation


