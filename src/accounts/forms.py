from django.forms import (Form, CharField, PasswordInput,)


class LoginForm(Form):

    username = CharField(required=True, label='Имя пользователя')
    password = CharField(required=True, label='Пароль', widget=PasswordInput)
