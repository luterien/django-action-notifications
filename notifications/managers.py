
from django.db.models import Manager
from django.contrib.contenttypes.models import ContentType


class GenericManager(Manager):

    def new(self, actor, action_object, verb, target=None):

        item = self.model(
            actor_content_type=ContentType.objects.get_for_model(actor),
            actor_object_id=actor.pk,
            action_object_content_type=ContentType.objects.get_for_model(
            	action_object),
            action_object_id=action_object.pk,
            verb=verb
        )

        if target:
            item.target_content_type = ContentType.objects.get_for_model(
            	target)
            item.target_object_id = target.pk
        
        return item
