


Usage
=====


INSTALLED_APPS = (

	...

	'notifications',

)


NOTIFICATIONS = {
	
	"notify_on_action": True,

}


calling create_action method;

# create_action(actor, action_object, verb, target)


example;

from notifications.notify import create_action

create_action(user, another_user, "accepted", friendship_request)

