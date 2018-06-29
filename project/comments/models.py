# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', verbose_name=u'Автор')
    question = models.ForeignKey('questions.Question', related_name='comments', verbose_name=u'Вопрос')
    #name = models.CharField(max_length=255, verbose_name=u'Заголовок комментария')
    is_archive = models.BooleanField(default=False, verbose_name=u'Комментарий в архиве')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name=u'Комментарий')

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = 'author', 'id'

    def __unicode__(self):
        return self.text