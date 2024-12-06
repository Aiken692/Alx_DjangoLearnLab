from django.apps import AppConfig


class BlogAppConfig(AppConfig):  # Ensure this class name matches your app name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'  # Ensure the name matches your app directory

    def ready(self):
        import blog.signals
