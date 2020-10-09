from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """Makes sure that profile is created when user is created look for signal.py for more information"""
        import users.signals
