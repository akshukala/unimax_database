from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    shop_name = models.TextField(blank=True, null=True)
    person_name = models.CharField(max_length=512, null=True, blank=True)
    contact_no = models.CharField(max_length=15)
    area = models.CharField(max_length=512)
    address = models.TextField(blank=True, null=True)
    gst_no = models.CharField(max_length=15, blank=True, null=True)
    pan_no = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, related_name="customer_entered_by")
    modified_by = models.ForeignKey(User, null=True, related_name="customer_modified_by")

class CustOrder(models.Model):
	PAYMENT_TYPE = ((1, "Credit"),
				   (2, "Immediate"))
	status = models.CharField(max_length=128, default="CREATED")
	remarks = models.TextField(blank=True, null=True)
	owner = models.ForeignKey(Customer)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	payment_type = models.IntegerField(choices=PAYMENT_TYPE)
	created_by = models.CharField(max_length=512)
	modified_by = models.CharField(max_length=512)
	grand_total = models.FloatField(default=0)
	is_active = models.BooleanField(default=True)

class Order_Item(models.Model):
	order = models.ForeignKey(CustOrder)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	item_name = models.CharField(max_length=512)
	quantity = models.IntegerField(default=1)
	selling_price = models.FloatField(default=0)
	total_price = models.FloatField(default=0)


class User_Details(models.Model):
	executive_name = models.CharField(max_length=512)
	password = models.CharField(max_length=512)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	user = models.ForeignKey(User)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

class Shop_Images(models.Model):
	img_url = models.CharField(max_length=1024, blank=True, null=True)
	customer = models.ForeignKey(Customer)
