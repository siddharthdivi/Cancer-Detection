# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.

from prime.models import Doctor,Test

admin.site.register(Doctor)
admin.site.register(Test)
