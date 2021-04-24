from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from images.models import Image

@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()

# m2m_changed - это наш сигнал
# декоратор receiver принимает сигналы

# 1) мы регистрируем функцию users_like_changed как нащ подписчик с помощью декоратора receiver.
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

