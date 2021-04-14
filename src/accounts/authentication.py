from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuthBackend:

    def authenticate(self, request, username=None, password=None):
        user = User.objects.filter(email=username).first()
        if user:
            if not user.check_password(password):
                return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# Для собственной аутентификации достаточно определить два метода:
# authenticate() и get_user()
# authenticate() - должен возвращать объект User и проверять то что пароль соответствует юзернейму
# для этого мы используем крутую и нужную функцию (метод для объекта user) check_password()

# фукнция check_password - шифрует пароль (возможно хеширует),
# и проверяет равен ли паролю, полученному у пользователя (тот то хранится в бд)

# но эта функкция может быть импортирована из
# from django.contrib.auth.hashers import check_password
# и тогда она будет принимать два пароля как аргумент и сравнивает их
# check_password(password1, password2)
# дальше мы регистрируем наш класс в settings
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'accounts.authentication.EmailAuthBackend',
# ]
# Первый backend там встроенный, второй наш, который мы определили

# про get_user(), почему он принимает только id и зачем он здесь нужен - хз

# Если в кратце:
# 1) добавляем AUTHENTICATION_BACKENDS в settings с базовой аутентификацией
# 2) определяем в каком-нибудь файле свою аутентификацию (authentication backend)
# 3) эта аутентификация должна быть классом и содержать два метода authenticate() и get_user()
# 4) в authenticate мы должны вернуть объект юзера и проверить что ему сооветствует пароль
# с помощью функции check_password()
# 5) добавить наш класс в AUTHENTICATION_BACKENDS и путь до него ('accounts.authentication.EmailAuthBackend')
# 6) все это влияет в коненом счете (скорее всего!!) на функцию authenticate() from django.contrib.auth
# скорее всего эта функция будет пробегаться по AUTHENTICATION_BACKENDS, но это не точно