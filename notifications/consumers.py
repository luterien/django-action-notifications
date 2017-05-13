import json

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group


def ws_message(message):
	Group("notifications").send({
			"text": message.content['text'],
		})


def ws_connect(message):
	message.reply_channel.send({"accept": True})
	Group("notifications").add(message.reply_channel);


def _send_notification_to_socket(notification_data):
	Group("notifications").send({
			"text": json.dumps(notification_data)
		})

