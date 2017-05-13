
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext as _
from django.utils import timezone

from .managers import GenericManager
from .utils import get_format


class BaseAction(models.Model):

    # Actor
    actor_content_type = models.ForeignKey(ContentType, 
        related_name="%(app_label)s_%(class)s_actor_type")
    
    actor_object_id = models.TextField(_('object id'))
    actor = GenericForeignKey('actor_content_type', 'actor_object_id')

    # Action
    action_object_content_type = models.ForeignKey(ContentType, 
        related_name="%(app_label)s_%(class)s_action_type", blank=True, null=True)

    action_object_id = models.TextField(_('object id'), blank=True, null=True)
    action_object = GenericForeignKey('action_object_content_type', 'action_object_id')

    # Target
    target_content_type = models.ForeignKey(ContentType, 
        related_name="%(app_label)s_%(class)s_target_type", blank=True, null=True)

    target_object_id = models.TextField(_('object id'), blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')

    date_created = models.DateTimeField(default=timezone.now)

    verb = models.CharField(max_length=100)

    objects = GenericManager()

    class Meta:
        abstract = True
        ordering = ("-date_created",)

    def __str__(self):

        dx = {
            'actor': self.actor,
            'verb': self.verb,
            'action': self.action_object,
            'target': self.target
        }

        display_format = get_format(self)

        return display_format % dx

