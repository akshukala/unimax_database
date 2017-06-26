# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0003_transaction_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_mode',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
