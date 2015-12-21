from django.db.models.signals import pre_save
from django.dispatch import receiver

from proxy.models import History


@receiver(pre_save, sender=History)
def pre_save_history(sender, instance, *args, **kwargs):
    # Remove appended slash on url.
    # For example, save "https://okwarning.or.kr/" as "https://okwarning.or.kr".

    if instance.url[-1] == '/':
        instance.url = instance.url[:-1]
