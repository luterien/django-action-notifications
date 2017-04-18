# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from utils import get_format, send_notification
from base_models import BaseAction
from managers import ActionManager


class Action(BaseAction):

	"""

		Logs a user's actions.

		User action examples:
    
	        <ahmet> has <deleted> <discussionTitle>
	        <ercan> has <commented> <on> <taskTitle>
	        <erhan> has <created> <projectTitle>
	        <murat> has <assigned> <username> to <taskName>
	        <ayhan> has <changed> <taskTitle>

	"""

    is_active = models.BooleanField(default=True)

    objects = ActionManager()


class Notification(BaseAction):

	"""

		Stores notification data sent to each recipient for actions created

	"""

	recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications')

	is_seen = models.BooleanField(default=False)


