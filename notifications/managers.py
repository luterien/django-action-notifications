
from django.db.models import Manager
from django.contrib.contenttypes.models import ContentType


class ActionManager(Manager):

    def new_action(self, actor, action, target=None):

        """
            Create a new action
        """

        action = self.model(
            actor_content_type=ContentType.objects.get_for_model(actor),
            actor_object_id=actor.pk,
            action_object_content_type=ContentType.objects.get_for_model(
            	action_object),
            action_object_id=action_object.pk
        )

        if target:
            action.target_content_type = ContentType.objects.get_for_model(
            	target)
            action.target_object_id = target_object.pk

        action.save()
        
        return action

