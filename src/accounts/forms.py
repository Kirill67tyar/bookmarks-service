from django.contrib.auth.models import User
from django.forms import (Form, ModelForm, CharField, PasswordInput, ValidationError, TextInput)
from accounts.models import Profile

attrs = {
    'attrs': {
        'placeholder': 'Enter username or email'
    }
}

class LoginForm(Form):

    username = CharField(required=True, label='Имя пользователя или email', widget=TextInput(**attrs))
    password = CharField(required=True, label='Пароль', widget=PasswordInput)


class RegisterModelForm(ModelForm):

    password = CharField(widget=PasswordInput, label='Введите пароль')
    password2 = CharField(widget=PasswordInput, label='Введите пароль еще раз')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise ValidationError('Пароли должны совпадать')
        return cd.get('password2')


class UserEditModelForm(ModelForm):

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email',



class ProfileEditModelForm(ModelForm):

    class Meta:
        model = Profile
        fields = 'date_of_birth', 'photo',
