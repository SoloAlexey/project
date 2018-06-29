# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = 'text', 'author', 'question'
    search_fields = 'name', 'author__username', 'question__name'
    list_filter = 'is_archive',
