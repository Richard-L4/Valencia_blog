from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the 'about' application.

    This class tells Django how to configure some aspects of the 'about' app.
    It's automatically used when the app is listed in INSTALLED_APPS.
    """
    # Specifies the type of primary key to use for models in this app.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the app (must match the folder name or module path).
    name = 'about'
