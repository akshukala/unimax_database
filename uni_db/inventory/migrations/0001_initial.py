# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_erp', '0002_auto_20170612_0515'),
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barcode_no', models.CharField(unique=True, max_length=128)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(to='client_erp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_chalan', models.CharField(max_length=255, null=True, blank=True)),
                ('driver_name', models.CharField(max_length=255, null=True, blank=True)),
                ('delivery_by', models.CharField(max_length=256, null=True, blank=True)),
                ('total_weight', models.IntegerField(default=0)),
                ('order', models.OneToOneField(to='order_management.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0)),
                ('barcode', models.OneToOneField(to='inventory.Barcode')),
                ('delivery', models.ForeignKey(to='inventory.Delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('fulfilled_qty', models.IntegerField(default=0)),
                ('product', models.OneToOneField(to='client_erp.Product')),
            ],
        ),
    ]
