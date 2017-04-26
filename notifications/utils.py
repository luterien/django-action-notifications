
import settings as app_settings

from constants import BASIC, NO_TARGET


available_backends = ["database",]


def get_format(action):
    """

        find the suitable display format for the given action instance

    """
    if action.target:
        return app_settings.NOTIFICATION_FORMATS[BASIC]

    return app_settings.NOTIFICATION_FORMATS[NO_TARGET]


def send_notification_from_action(action, recepients):
    
    from models import Notification

    for recepient in recepients:

        Notification.objects.create()


def _get_backend():
    pass



