# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_remove_message_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None),
        ),
    ]
