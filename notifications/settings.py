from django.conf import settings

from constants import default_formats


try:
	NOTIFICATION_FORMATS = settings.NOTIFICATIONS["formats"]
except AttributeError:
	NOTIFICATION_FORMATS = default_formats["default"]

try:
	NOTIFY_ON_ACTION = settings.NOTIFICATIONS["notify_on_action"]
except AttributeError:
	NOTIFY_ON_ACTION = True

