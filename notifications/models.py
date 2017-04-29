# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from consumers import _send_notification_to_socket
from base_models import BaseAction


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


class Notification(BaseAction):

    """

        Stores notification data sent to each recipient for actions created

    """

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications')

    is_seen = models.BooleanField(default=False)

    def unread_for_recipient(self):
        return self.recipient.notifications.filter(is_seen=False).count()


@receiver(post_save, sender=Notification)
def send_live_notification(sender, instance, **kwargs):
    _send_notification_to_socket(instance.unread_for_recipient())





































