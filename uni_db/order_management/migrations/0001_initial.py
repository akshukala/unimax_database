# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client_erp', '0002_auto_20170612_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('sales_order_id', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.CharField(default='CREATED', max_length=20)),
                ('remarks', models.TextField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('cash_on_delivery', models.BooleanField(default=True)),
                ('order_discount', models.FloatField(default=0)),
                ('total_discount', models.FloatField(default=0)),
                ('internal_note', models.CharField(max_length=1024, null=True, blank=True)),
                ('advance_payment', models.FloatField(default=0)),
                ('adv_pay_note', models.CharField(max_length=1024, null=True, blank=True)),
                ('grand_total', models.FloatField(default=0)),
                ('cod_amount', models.FloatField(default=0)),
                ('advance_order_date', models.DateField(null=True, blank=True)),
                ('billing_address', models.ForeignKey(to='client_erp.BillingAddress')),
                ('entered_by', models.ForeignKey(related_name='order_entered_by', to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='order_modified_by', to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(to='client_erp.Client')),
                ('shipping_address', models.ForeignKey(to='client_erp.ShippingAddress')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('item_name', models.CharField(max_length=512)),
                ('status_code', models.CharField(default='CREATED', max_length=128)),
                ('quantity', models.IntegerField(default=1)),
                ('list_price', models.FloatField(null=True, blank=True)),
                ('selling_price', models.FloatField()),
                ('discount', models.FloatField(default=0)),
                ('adj_discount', models.FloatField(default=0)),
                ('prepaid_amount', models.FloatField(default=0)),
                ('total_price', models.FloatField()),
                ('order', models.ForeignKey(to='order_management.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(to='order_management.Order')),
            ],
        ),
    ]
