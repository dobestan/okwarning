from django.apps import AppConfig


class ProxyAppConfig(AppConfig):
    name = 'proxy'

    def ready(self):
        from .signals.pre_save import pre_save_history
