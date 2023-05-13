from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "djagno_instar_clone.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import djagno_instar_clone.users.signals  # noqa: F401
        except ImportError:
            pass
