# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Notification


def main(request):
	return render(request, "hello.html", {
			"count": 0
		})

