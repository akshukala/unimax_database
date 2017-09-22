# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0004_auto_20170626_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_no',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
