from django.contrib import admin

# Register your models here.
from .models import userGeneralInformation, userJob, userQualifications, UserPictures

class userGeneralInformationAdmin(admin.ModelAdmin):	
	class Meta:
		model = userGeneralInformation

admin.site.register(userGeneralInformation, userGeneralInformationAdmin)

class userJobAdmin(admin.ModelAdmin):	
	class Meta:
		model = userJob

admin.site.register(userJob, userJobAdmin)

class userQualificationsAdmin(admin.ModelAdmin):	
	class Meta:
		model = userQualifications

admin.site.register(userQualifications, userQualificationsAdmin)

class PicturesAdmin(admin.ModelAdmin):	
	class Meta:
		model = UserPictures


admin.site.register(UserPictures, PicturesAdmin)
