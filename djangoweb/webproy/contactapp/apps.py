from django.apps import AppConfig

class ContactAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactapp'  # Nombre de la app, debe coincidir con el nombre de la carpeta
    verbose_name = 'Contact App'  # Nombre descriptivo de la app para la interfaz de usuario
