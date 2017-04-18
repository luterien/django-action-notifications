-- currently under development --

Add app name to settings.py

INSTALLED_APPS = (

	...

	'notifications',

)

call send_notification function

from notifications.notify import send_notification
send_notification(actor=actor, action=action_object, verb="", recipients=[], target=target)

