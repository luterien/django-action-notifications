# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Notification, Action


admin.site.register(Notification)
admin.site.register(Action)

