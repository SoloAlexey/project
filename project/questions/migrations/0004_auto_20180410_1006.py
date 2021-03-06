# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 10:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20180410_0707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('name', 'id'), 'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441', 'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b'},
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='question',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='questions', to='categories.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441 \u0432 \u0430\u0440\u0445\u0438\u0432\u0435'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432\u043e\u043f\u0440\u043e\u0441\u0430'),
        ),
    ]
