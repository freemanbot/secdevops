from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "secdevops.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
