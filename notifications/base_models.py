
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_unicode
from django.utils import timezone


class BaseAction(models.Model):

	# Actor
    actor_content_type = models.ForeignKey(ContentType, related_name="actor_object")
    actor_object_id = models.TextField(_('object id'))
    actor = generic.GenericForeignKey('actor_content_type', 'actor_object_id')

    # Action
    action_object_content_type = models.ForeignKey(ContentType, related_name="action_object", blank=True, null=True)
    action_object_id = models.TextField(_('object id'), blank=True, null=True)
    action_object = generic.GenericForeignKey('action_object_content_type', 'action_object_id')

    # Target 
    target_content_type = models.ForeignKey(ContentType, related_name="target_object", blank=True, null=True)
    target_object_id = models.TextField(_('object id'), blank=True, null=True)
    target = generic.GenericForeignKey('target_content_type', 'target_object_id')

    date_created = models.DateTimeField(default=timezone.now)

    verb = models.CharField(max_length=100)

    class Meta:
    	abstract = True
    	ordering = ("-date_created",)

    def __str__(self):

    	dx = {
            'actor': self.actor,
            'verb': self.verb,
            'action_object': self.action_object,
            'target': self.target
        }

        display_format = get_format()

    	return display_format % dx

