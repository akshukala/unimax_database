# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_name', models.TextField(null=True, blank=True)),
                ('person_name', models.CharField(max_length=512, null=True, blank=True)),
                ('contact_no', models.CharField(max_length=15)),
                ('area', models.CharField(max_length=512)),
                ('address', models.TextField(null=True, blank=True)),
                ('gst_no', models.CharField(max_length=15, null=True, blank=True)),
                ('pan_no', models.CharField(max_length=10, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='customer_entered_by', to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='customer_modified_by', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'CREATED', max_length=128)),
                ('remarks', models.TextField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('payment_type', models.IntegerField(choices=[(1, b'Credit'), (2, b'Immediate')])),
                ('created_by', models.CharField(max_length=512)),
                ('modified_by', models.CharField(max_length=512)),
                ('grand_total', models.FloatField(default=0)),
                ('owner', models.ForeignKey(to='mob_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('item_name', models.CharField(max_length=512)),
                ('quantity', models.IntegerField(default=1)),
                ('selling_price', models.FloatField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('order', models.ForeignKey(to='mob_app.CustOrder')),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('executive_name', models.CharField(max_length=512)),
                ('password', models.CharField(max_length=512)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
