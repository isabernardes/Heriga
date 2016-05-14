from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL



def upload_location(instance, filename):
	location = str(instance.user.username)
	return "%s/%s" %(location, filename)


class userGeneralInformation (models.Model):
	user = models.OneToOneField(User)
	dateofbirth = models.DateField(null=True, blank=True)
	cityOfBirth  = models.CharField(max_length=50, null=True, blank=True)
	countryOfBirth = models.CharField(max_length=50, null=True, blank=True)
	cityofResidence = models.CharField(max_length=50, null=True, blank=True)
	countryofResidence = models.CharField(max_length=50, null=True, blank=True)
	active = models.BooleanField(default=True)

	def __unicode__(self, ):
			return self.cityofResidence

class userJob (models.Model):
	user = models.ForeignKey(User)
	occupation = models.CharField(max_length=100, null=True, blank=True)
	placeOfWork = models.CharField(max_length=100, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
	

class userQualifications (models.Model):
	user = models.ForeignKey(User)
	university = models.CharField(max_length=100, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True) 

	def __unicode__(self, ):
			return self.university

class userLanguages (models.Model):
	user = models.ForeignKey(User)
	languages = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self, ):
			return self.languages	


class UserPictures (models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

   	def __unicode__(self, ):
        	return str(self.image)

