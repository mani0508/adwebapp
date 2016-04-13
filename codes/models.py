from django.db import models

from django.utils import timezone
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.validators import RegexValidator



# Create your models here.

class Category(models.Model):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=200)
	description = models.TextField(max_length=1000, blank = True)

class OutdoorType(models.Model):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length =50)
	description = models.TextField(max_length=500,blank=True)

class LighteningType(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=50)
	description = models.TextField(max_length = 500, blank= True)

class State(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length = 40)
class City (models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=80)

class Owner(models.Model):
	def __unicode__(self):
		return self.owner_name
	username = models.CharField(max_length=50, primary_key = True)
	owner_name = models.CharField(max_length=80,blank = True)
	agency_name = models.CharField(max_length=200)
	contact_person_name = models.CharField(max_length= 80,blank=True)
	contact_person_number = models.CharField(max_length=12,validators=[MinLengthValidator(10)])
	alternate_number = models.CharField(max_length=12,validators=[MinLengthValidator(10)], blank=True)
	email = models.EmailField(max_length=60)
	address = models.CharField(max_length=300)
	city = models.ForeignKey(City)
	pin = models.CharField(max_length=6,validators=[MinLengthValidator(6)])
	id_type = models.CharField(max_length=200,choices=[('Aadhar card','Aadhar card'),('Driving License','Driving License'),('Passport','Passport'),('Election id','Election id'),('Ration Card','Ration Card')])
	id_number = models.CharField(max_length=25, blank=True)
	service_tax_number = models.CharField(max_length=25,blank = True)
	vat_number = models.CharField(max_length=25,blank = True)
	pan_number = models.CharField(max_length=15,blank = True)
	account_number = models.CharField(max_length=25,blank = True)
	ifsc = models.CharField(max_length=15, blank=True)

class Hoarding(models.Model):
	def __unicode__(self):
		return self.hoarding_id

	hoarding_id = models.CharField(max_length=200,primary_key = True)
	owner = models.ForeignKey(Owner)
	category = models.ForeignKey(Category , blank = True)
	hoarding_type = models.ForeignKey(OutdoorType , blank = True)
	lightening = models.ForeignKey(LighteningType)
	address = models.CharField(max_length =300)
	city = models.ForeignKey(City)
	state = models.ForeignKey(State)
	pin = models.CharField(max_length=6,validators=[MinLengthValidator(6)], blank = True)
	area = models.CharField(max_length = 200 , blank = True)
	landmark = models.CharField(max_length=100 , blank = True)
	facing_from = models.CharField(max_length=200,default = 'Not Available' , blank = True)
	facing_to = models.CharField(max_length=200, default = 'Not Available' , blank = True)
	length = models.DecimalField(max_digits = 7, decimal_places = 2)
	width = models.DecimalField(max_digits = 7, decimal_places = 2)
	elevation = models.DecimalField(max_digits = 7, decimal_places = 2 , blank = True)
	available_from = models.DateField(auto_now=False, auto_now_add=False , null = True)
	available_to = models.DateField(auto_now=False, auto_now_add=False)
	available = models.CharField(max_length=10, choices = [('yes','YES'),('no','NO')],default = 'yes')
	trafic_signal = models.CharField(max_length=10, choices = [('yes','YES'),('no','NO')],default = 'no')
	speciality = models.CharField(max_length=200, blank = True)
	price_per_month = models.CharField(max_length = 15 , blank = True)
	image1 = models.ImageField(upload_to = '/home/mani/vishal/media/images',blank=True)
	image2 = models.ImageField(upload_to = '/home/mani/vishal/media/images',blank=True)
	image3 = models.ImageField(upload_to = '/home/mani/vishal/media/images',blank=True)
	image4 = models.ImageField(upload_to = '/home/mani/vishal/media/images',blank=True)
	description = models.TextField(max_length=1000, blank=True)


class Customer(models.Model):
	def __unicode__(self):
		return self.owner_name
	username = models.CharField(max_length=50, primary_key = True)
	buyer_name = models.CharField(max_length=80,blank = True)
	company_name = models.CharField(max_length=200)
	contact_person_name = models.CharField(max_length= 80,blank=True)
	contact_person_number = models.CharField(max_length=12,validators=[MinLengthValidator(10)])
	alternate_number = models.CharField(max_length=12,validators=[MinLengthValidator(10)], blank=True)
	email = models.EmailField(max_length=60)
	address = models.CharField(max_length=300)
	city = models.ForeignKey(City)
	pin = models.CharField(max_length=6,validators=[MinLengthValidator(6)])
	id_type = models.CharField(max_length=200,choices=[('Aadhar card','Aadhar card'),('Driving License','Driving License'),('Passport','Passport'),('Election id','Election id'),('Ration Card','Ration Card')])
	id_number = models.CharField(max_length=25, blank=True)
	service_tax_number = models.CharField(max_length=25,blank = True)
	vat_number = models.CharField(max_length=25,blank = True)
	pan_number = models.CharField(max_length=15,blank = True)
	account_number = models.CharField(max_length=25,blank = True)
	ifsc = models.CharField(max_length=15, blank=True)

class Location(models.Model):
	def __unicode__(self):
		return self.hoarding_id
	hoarding_id = models.ForeignKey(Hoarding)
	latitude = models.DecimalField(max_digits = 20,decimal_places=15)
	longitude = models.DecimalField(max_digits = 20,decimal_places=15)

class UserProfile(models.Model):
	def __unicode__(self):
		return self.username
	username = models.CharField(max_length=30)
	user_type = models.CharField(max_length=10, choices = [('admin','Admin'),('owner','Owner'),('broker','Broker'),('customer','Customer')])
	name = models.CharField(max_length = 70 , blank = True)
	password = models.CharField(max_length = 35 , blank =True)



class Transaction(models.Model):
	def __unicode__(self):
		return self.trans_id

	tran_id = models.AutoField(primary_key=True)
	customer = models.ForeignKey(Customer)
	hoardings = models.ManyToManyField(Hoarding)
	total_price = models.IntegerField()
	paid = models.IntegerField()
	customer_contact_person_name = models.CharField(max_length= 50)
	customer_contact_person_number = models.CharField(max_length=12,validators=[MinLengthValidator(10)])
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Hoarding_Customer(models.Model):
	def __unicode__(self):
		return self.hoarding_id
	hoarding_id = models.CharField(max_length=50)
	tran_id = models.ForeignKey(Transaction)
	from_date = models.DateField()
	to_date = models.DateField()
	status = models.CharField(max_length=20,choices=[('confirm','confirm'),('closed','closed'),('cancel','cancel')])
