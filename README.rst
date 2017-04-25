**this repository is currently under development**

Add app name to settings.py;

.. code-block:: python

	INSTALLED_APPS = (

		...

		'notifications',

	)

call send_notification function;

.. code-block:: python

    from notifications.notify import send_notification
    send_notification(actor=actor, action=action_object, verb="", recipients=[], target=target)

an example would be like this;

.. code-block:: python

   from notifications.notify import send_notification
   
   def club_invitation_assignment(club_member, new_club_member, club_object):
   
        send_notification(
	    actor=club_member,
	    action=new_club_member,
	    verb="invited",
	    recipients=club_object.members,
	    target=club_object
	)
	 
	 
Using the default format ("%(actor)s %(verb)s %(action)s on %(target)s") this would print something like;

- club_member invited new_club_member on club_object.

Which is not really what we want...So we can add a new format for this verb to our settings.py, like this;

.. code-block:: python

   NOTIFICATIONS = {
        "formats": {
	    "invited" : {
		"basic" : "%(actor)s %(verb)s %(action)s to %(target)s.",
		"no_target" : "%(actor)s %(verb)s %(action)s to a random club."
	    }
	}
   }
	    




