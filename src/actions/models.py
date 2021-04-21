from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Action(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions', db_index=True, verbose_name='Юзер')
    verb = models.CharField(max_length=255, verbose_name='Действие')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Было соверешено')

    class Meta:
        ordering = '-created',

    def __str__(self):
        return self.verb
