from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class MyPasswordChangeView(auth_views.PasswordChangeView):

    success_url = reverse_lazy('accounts:password_change_done')
