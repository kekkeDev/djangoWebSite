from django.apps import AppConfig
from django.db.models.signals import post_migrate

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        from .models import create_default_site_detail
        post_migrate.connect(create_default_site_detail, sender=self)