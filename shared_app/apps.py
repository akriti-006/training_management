from django.apps import AppConfig


class SharedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared_app'

    def ready(self):
        import shared_app.signals  