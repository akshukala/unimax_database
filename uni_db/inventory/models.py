from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User
from uni_db.client_erp.models import Product
from uni_db.order_management.models import Order


class Stock(models.Model):
	product=models.OneToOneField(Product)
	quantity=models.IntegerField(default=0)
	fulfilled_qty=models.IntegerField(default=0)

class Barcode(models.Model):
	barcode_no=models.CharField(max_length=128,unique=True)
	product=models.ForeignKey(Product)
	created_on=models.DateTimeField(auto_now_add=True)
	
class Delivery(models.Model):
	order=models.OneToOneField(Order)	
	delivery_chalan=models.CharField(max_length=255,null=True,blank=True)
	driver_name=models.CharField(max_length=255,null=True,blank=True)
	delivery_by=models.CharField(max_length=256,null=True,blank=True)
	total_weight=models.IntegerField(default=0)
	# to_channel_partner = models.CharField(max_length=255,null=True,blank=True)
	
# class IndiaPostBarcode(models.Model):
# 	INDIAPOST_TYPE = ((1,"BPCOD"),
#                       (2,"SPCOD"),
#                       (3,"NONCOD"))
# 	ip_barcode = models.CharField(max_length=256)
# 	order = models.OneToOneField(Order,null=True,blank=True)
# 	is_used = models.BooleanField(default=False)
# 	india_post_type=models.IntegerField(choices=INDIAPOST_TYPE,default=1)
# 	order_dict = JSONField(blank=True,null=True)
	
class OrderItemDetails(models.Model):
	barcode = models.ForeignKey(Barcode)
	delivery = models.ForeignKey(Delivery)
	weight=models.IntegerField(default=0)
	
