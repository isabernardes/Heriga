from django.db import models

# Create your models here.
# MVC MODEL VIEW CONTROLLER

class Communities(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	#timestamp
	

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name