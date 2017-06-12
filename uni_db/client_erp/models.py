from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)


# class Seller(models.Model):
#     name = models.CharField(max_length=255)
#     seller_code = models.CharField(max_length=255, null=True, blank=True)
#     address = models.TextField(max_length=2048, null=True, blank=True)
#     vat = models.CharField(max_length=255, null=True, blank=True)
#     pan = models.CharField(max_length=255, null=True, blank=True)


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(ProductCategory)
    # seller = models.ForeignKey(Seller)
    mrp = models.FloatField()
    selling_price = models.FloatField()
    weight = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    gst = models.CharField(max_length=50, null=True, blank=True)

class Agent(models.Model):
    user = models.OneToOneField(User)
    mobile_no = models.CharField(max_length=13)
    # sr_api_key = models.CharField(max_length=255)


# class PostCallDetails(models.Model):
#     phone = models.CharField(max_length=255)
#     call_type = models.CharField(max_length=255)
#     replied_back = models.BooleanField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     assigned_to = models.ForeignKey(Agent, null=True)
#     call_count = models.IntegerField(default=0)

# class PostCallTags(models.Model):
#     postcall = models.OneToOneField(PostCallDetails)
#     user = models.ForeignKey(User)
#     remarks = models.CharField(max_length=255)
    
# class Language(models.Model):
#     lang_code = models.CharField(max_length=10, blank=True)
#     lang_name = models.CharField(max_length=128)


# class PostalAddress(models.Model):
#     state = models.CharField(max_length=31)
#     district = models.CharField(max_length=31)
#     taluka = models.CharField(max_length=31)
#     post_office = models.CharField(db_index=True, max_length=63)
#     pin_code = models.CharField(max_length=8)

    # class Meta:
    #     index_together = [
    #         ["state", "district", "taluka", "post_office"],
    #     ]


class Client(models.Model):
    client_id = models.AutoField(primary_key=True, max_length=31)
    client_name = models.CharField(db_index=True, max_length=256, null=True, blank=True) 
    heard_about = models.CharField(max_length=50, null=True, blank=True)
    referer = models.CharField(max_length=31, null=True, blank=True)
    # mobile_1 = models.CharField(
    #     db_index=True, max_length=15, null=True, blank=True)
    # mobile_2 = models.CharField(
    #     db_index=True, max_length=15, null=True, blank=True)
    # mobile_3 = models.CharField(
    #     db_index=True, max_length=15, null=True, blank=True)
    # smslang_1 = models.CharField(max_length=32, null=True, blank=True)
    # smslang_2 = models.CharField(max_length=32, null=True, blank=True)
    # smslang_3 = models.CharField(max_length=32, null=True, blank=True)

    billing_addressid = models.IntegerField(null=True, blank=True)
    shipping_addressid = models.IntegerField(null=True, blank=True)
    entered_by = models.ForeignKey(User, null=True, blank=True, related_name="client_entered")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name="client_modified")

    # crop_insurance = models.BooleanField(default=False)
    # tractor = models.BooleanField(default=False)
    # drip_irrigation = models.BooleanField(default=False)


    def client_history(self):
        return ClientStatusHistory.objects.filter(client=self).order_by('-id')
    
    def save(self, *args, **kwargs):

        super(Client, self).save(*args, **kwargs)
        
        client_history=self.client_history()
        if not client_history or self.modified_by!= client_history[0].user:
            client_historyObj =ClientStatusHistory(client=self,user=self.modified_by) 
            client_historyObj.save()

class ClientStatusHistory(models.Model):
    client = models.ForeignKey(Client)
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now=True)

class ClientMobile(models.Model):
	client = models.ForeignKey(Client)
	mobile = models.CharField(db_index=True, max_length=15)

class ClientWhatsapp(models.Model):
	client = models.ForeignKey(Client)
	whatsapp = models.CharField(db_index=True, max_length=15)		

class ClientLandline(models.Model):
	client = models.ForeignKey(Client)
	landline = models.CharField(db_index=True, max_length=15)

class Address(models.Model):
    client = models.ForeignKey(Client)
    state = models.CharField(max_length=31)
    city = models.CharField(max_length=31)
    area = models.CharField(max_length=31)
    pin_code = models.CharField(max_length=8, null=True, blank=True)
    address_line1 = models.TextField()
    country = models.CharField(max_length=64, blank=True, default="IN")

    class Meta:
        abstract = True

class BillingAddress(Address):
    pass


class ShippingAddress(Address):
    pass

# class CropInformation(models.Model):
#     farmer = models.ForeignKey(Farmer, db_index=True)
#     crop = models.CharField(max_length=32)
#     season = models.CharField(max_length=15, null=True, blank=True)
#     area = models.DecimalField(
#         max_digits=16, decimal_places=2, null=True, blank=True)
#     unit = models.CharField(max_length=16, null=True, blank=True)
#     active = models.BooleanField(default=True)
#     is_future = models.BooleanField(default=False)

# class Crop(models.Model):
#     crop_name = models.CharField(max_length=32)
#     verified_state = models.CharField(max_length=3)


class ClientComment(models.Model):
    client = models.ForeignKey(Client, db_index=True)
    commented_by = models.ForeignKey(User)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=2048, null=True, blank=True)


class AddCall(models.Model):
    client = models.ForeignKey(Client)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True)


class CallTag(models.Model):
    call = models.ForeignKey(AddCall)
    tags = models.TextField(max_length=2048, null=True, blank=True)


class Tags(models.Model):
    tag_name = models.TextField(max_length=2048)
    tag_description = models.TextField(max_length=2048)

class ScheduleCalls(models.Model):
    phone = models.CharField(max_length=255)
    replied_back = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    schedule_date = models.DateTimeField(blank=True ,null = True)
    associated_to = models.ForeignKey(Agent, null=True)
    note = models.TextField(null=True, blank=True)

# class MessageTracking(models.Model):
#     phone = models.CharField(max_length=255)
#     msg_count = models.IntegerField(default=0)
#     last_replied_back = models.ForeignKey(PostCallDetails, blank=True, null=True)
#     msg_status = models.BooleanField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
#     is_archived = models.BooleanField(default=False)