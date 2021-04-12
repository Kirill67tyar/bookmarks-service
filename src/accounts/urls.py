from django.contrib.auth import views as auth_views
from django.urls import path
from accounts.views import login_view, dashboard_view
from accounts.utils import MyPasswordChangeView
app_name = 'accounts'


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    # path('login/', login_view, name='login'),

    # Аутентификация из коробки ----------------------------------
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password-change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]
