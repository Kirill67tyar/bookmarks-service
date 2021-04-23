from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from datetime import timedelta

from actions.models import Action


def create_action(user, verb, target=None):
    """

    :param user: Объект User
    :param verb: что сделал User
    :param target: target - определенная модель
    :return: True если небыло идентиных действий больше 1 минуты, False в обратном случае
    """
    now = timezone.now()
    minute = timedelta(seconds=60)
    last_minute = now - minute
    # устанавливаем параметры (именованные аргументы) для фильтрации
    kwargs = {
        'user_id': user.pk,
        'verb': verb,
        'created__gte': last_minute, # созданы менее минуты назад
    }
    # находим индентиные запросы, сохраненные в бд за последние 60 секунд
    similar_actions = Action.objects.filter(**kwargs)

    if target:
        target_ct = ContentType.objects.get_for_model(model=target)
        # находим идентичные запросы если был target
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.pk)

    if not similar_actions:
        # если идентичных запросов не было хотя бы минуту - сохраняем новые в бд и возвращаем True
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True

    # в противном слуае вернем False
    return False