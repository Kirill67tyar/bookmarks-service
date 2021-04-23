from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Action(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions', db_index=True, verbose_name='Юзер')
    verb = models.CharField(max_length=255, verbose_name='Действие')

    # target_ct привязывает наш экземпляр Action к конкретному экземпляру ContentType
    target_ct = models.ForeignKey(ContentType,
                                  on_delete=models.CASCADE,
                                  related_name='target_obj',
                                  blank=True, null=True)
    target_id = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    # target - связывает target_ct и target_id вместе (возможно как unique_together)
    # django не создает столбец GenericForeignKey на уровне бд.
    # вместо этого будут сохраняться значения target_ct и target_id
    target = GenericForeignKey('target_ct', 'target_id')

    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Было соверешено')

    class Meta:
        ordering = '-created',

    def __str__(self):
        return self.verb

# Возможно, то поле GenericForeignKey похоже на аттрибут unique_together в классе Meta
# django не создает столбец GenericForeignKey на уровне бд.
# вместо этого будут сохраняться значения target_ct и target_id
# GenericForeignKey - поле для обращения к его связанному объекту на основании его типа и ID