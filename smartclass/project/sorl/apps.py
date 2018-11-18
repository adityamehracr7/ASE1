from django.apps import AppConfig


class SorlConfig(AppConfig):
    name = 'sorl'

    def ready(self):
        import sorl.signals
