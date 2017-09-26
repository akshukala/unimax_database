# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mob_app', '0003_auto_20170926_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_url', models.CharField(max_length=1024, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='img_url1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='img_url2',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='img_url3',
        ),
        migrations.AddField(
            model_name='shop_images',
            name='customer',
            field=models.ForeignKey(to='mob_app.Customer'),
        ),
    ]
