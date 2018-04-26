# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mypost.models import *
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display=['title','created','modified','zhonglei']
    list_filter = ['zhonglei__name','biaoqian__name']
admin.site.register(Zhonglei)
admin.site.register(Biaoqian)
admin.site.register(Post,PostModelAdmin)