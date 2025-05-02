from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the 'blog' app.
    This class defines the application-specific
    settings for Django to recognize and manage the app properly.
    """

    # Specifies the type of auto-generated primary key field
    # to use for models in this app
    default_auto_field = 'django.db.models.BigAutoField'

    # Name of the application as used in INSTALLED_APPS
    name = 'blog'
