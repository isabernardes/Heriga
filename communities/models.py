from django.db import models

# Create your models here.
# MVC MODEL VIEW CONTROLLER

class Communities(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title