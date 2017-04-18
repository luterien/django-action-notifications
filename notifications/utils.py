
from django.conf import settings

from constants import LEVELS


available_backends = ["database",]


def get_format(action):

	"""
		find the suitable display format for the given action instance
	"""

	if action.target:
		return settings.FORMATS.get(LEVELS.BASIC, LEVELS.DEFAULT)

	return settings.FORMATS.get(LEVELS.NO_TARGET, LEVELS.DEFAULT)


def send_notification(action, receivers):
	pass


def action(**kwargs):

	"""

		creates a new action

		if NOTIFY_ON_ACTION is enabled,
		sends notification to recipient list

	"""

	from models import Action

	Action.objects.new_action(**kwargs)

	if settings.NOTIFY_ON_ACTION:
		send_notification(action, receivers)


def _get_backend():

	value = settings.NOTIFICATIONS.get("backend", "database")

	if not value in available_backends:
		raise Exception("Invalid backend value.")



