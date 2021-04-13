from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class MyPasswordChangeView(auth_views.PasswordChangeView):

    success_url = reverse_lazy('accounts:password_change_done')



class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')


class MyPasswordResetView(auth_views.PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')
