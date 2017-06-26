# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bank',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
