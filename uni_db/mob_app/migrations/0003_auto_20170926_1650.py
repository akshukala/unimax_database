# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mob_app', '0002_custorder_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='img_url1',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='img_url2',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='img_url3',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
    ]
