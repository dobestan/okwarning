from django.apps import AppConfig


class ProxyAppConfig(AppConfig):
    name = 'proxy'

    def ready(self):
        pass
