from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


# class YourAppNameConfig(AppConfig):
#     name = 'users'

#     def ready(self):
#         import users.signals