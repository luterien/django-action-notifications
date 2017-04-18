import settings as app_settings

from utils import send_notification_from_action
from models import Action, Notification


def create_action(actor, action, verb, target=None):
	"""

		creates a new action

		if NOTIFY_ON_ACTION is enabled,
		sends notification to recipient list

	"""
	action = Action.objects.new(actor=actor, action_object=action, verb=verb, target=target)
	action.save()

	if app_settings.NOTIFY_ON_ACTION:
		send_notification_from_action(action, receivers)


def send_notification(actor, action, verb, recipients, target=None):
	"""

		Send notification to recipients

	"""
	for recipient in recipients:

		n = Notification.objects.new(actor=actor, action_object=action, 
			verb=verb, target=target)
		n.recipient = recipient
		n.save()

	#Notification.objects.bulk_create(data)


