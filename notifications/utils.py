
import settings as app_settings


available_backends = ["database",]


def get_format(action):
    """

        find the suitable display format for the given action instance

    """
    if action.target:
        return app_settings.NOTIFICATION_FORMATS["basic"]

    return app_settings.NOTIFICATION_FORMATS["no_target"]


def send_notification_from_action(action, recepients):
    
    from models import Notification

    for recepient in recepients:

        Notification.objects.create()


def _get_backend():
    pass



