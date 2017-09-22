# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.utils import timezone
from jsonfield import JSONField
from django.contrib.auth.models import User
from uni_db.client_erp.models import Client, ShippingAddress, BillingAddress

# Create your models here.
class Order(models.Model):
    sales_order_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, default="CREATED")
    # after_dispatch_status = models.CharField(max_length=255, default="PENDING", blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(Client, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    shipping_address = models.ForeignKey(ShippingAddress,
                                         blank=False, null=False)
    billing_address = models.ForeignKey(BillingAddress,
                                        blank=False, null=False)
    cash_on_delivery = models.BooleanField(default=True)
    order_discount = models.FloatField(default=0)
    total_discount = models.FloatField(default=0)
    entered_by = models.ForeignKey(User, null=True, related_name="order_entered_by")
    modified_by = models.ForeignKey(User, null=True, related_name="order_modified_by")
    internal_note = models.CharField(max_length=1024, null=True, blank=True)
    # external_note = models.CharField(max_length=1024, null=True, blank=True)
    advance_payment = models.FloatField(default=0)
    adv_pay_note = models.CharField(max_length=1024, null=True, blank=True)
    grand_total = models.FloatField(default=0)
    cod_amount = models.FloatField(default=0)
    advance_order_date = models.DateField(blank=True ,null = True)
    invoice_no = models.CharField(max_length=25, blank=True, null=True)
    
    def status_history(self):
        return OrderStatusHistory.objects.filter(order=self).order_by('-id')
    
    def save(self, *args, **kwargs):
    	super(Order, self).save(*args, **kwargs)
        status_history=self.status_history()
        if not status_history or self.status!= status_history[0].status:
        	status_historyObj =OrderStatusHistory(order=self,status=self.status) 
        	status_historyObj.save()

    def as_json(self):
        return dict(Code=self.id,
                    Status=self.status,
                    CreatedOn=self.created_on.isoformat(),
                    UpdatedOn=self.updated_on.isoformat(),
                    CashOnDelivery=self.cash_on_delivery,
                    CurrencyCode=self.currency_code,
                    BillingAddress=self.billing_address.as_json(),
                    ShippingAddress=self.shipping_address.as_json())

class OrderStatusHistory(models.Model):
    order=models.ForeignKey(Order)
    status=models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):

    order = models.ForeignKey(Order)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length=512, blank=False, null=False)
    # item_sku = models.CharField(max_length=512, blank=False, null=False)
    status_code = models.CharField(max_length=128, default="CREATED")
    quantity = models.IntegerField(default=1)
    # cancellable = models.BooleanField(default=True)
    list_price = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=False, null=False)
    discount = models.FloatField(default=0)
    adj_discount = models.FloatField(default=0)
    prepaid_amount = models.FloatField(default=0)
    total_price = models.FloatField(blank=False, null=False)
    # on_hold = models.BooleanField(default=True)

class Transaction(models.Model):
    order=models.OneToOneField(Order)
    payment_mode = models.CharField(max_length=20,blank=True, null=True)
    transaction_note=models.TextField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    bank = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now=True)