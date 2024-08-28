from django.apps import AppConfig


class SabpaisaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sabpaisa_app'
    AUTH_USER_MODEL = 'sabpaisa_app.AyushUser'
