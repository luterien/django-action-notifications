from django.conf import settings

from constants import default_formats


NOTIFICATION_FORMATS = settings.NOTIFICATIONS.get("formats") or default_formats



