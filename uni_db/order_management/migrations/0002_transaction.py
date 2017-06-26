# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_mode', models.CharField(max_length=20)),
                ('transaction_note', models.TextField()),
                ('payment_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('order', models.OneToOneField(to='order_management.Order')),
            ],
        ),
    ]
