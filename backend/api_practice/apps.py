from django.apps import AppConfig


class ApiPracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_practice'

    def ready(self):
        import api_practice.singals