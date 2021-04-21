from django.contrib.auth import views as auth_views
from django.urls import path
from accounts.views import (login_view, dashboard_view,
                            register_view, edit_view,
                            user_list_view, user_detail_view,
                            user_follow_view)
from accounts.utils import (MyPasswordChangeView, MyPasswordResetConfirmView, MyPasswordResetView)

app_name = 'accounts'


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('edit/', edit_view, name='edit'),

    path('users/', user_list_view, name='user_list'),
    path('users/follow/', user_follow_view, name='user_follow'),
    path('users/<str:username>/', user_detail_view, name='user_detail'),

    # Аутентификация из коробки ----------------------------------
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Просто смена пароля -------------------------------------
    path('password-change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Смена утерянного пароля -------------------------------------
    # урлы смены пароля по почте если забыл пароль и встроенные обработчики
    path('password-reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # смотри на шаблоны html в templates/registration/ ...reset...html
    # они связаны с встроенными обработчиками из коробки
    # и обрати внимание, что в settings мы подключили
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # это для того, чтобы посылать письма не на почту а в консоль
    # а так, надо конечно настраивать почту


]
