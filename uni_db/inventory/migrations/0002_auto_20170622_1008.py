# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemdetails',
            name='barcode',
            field=models.ForeignKey(to='inventory.Barcode'),
        ),
    ]
