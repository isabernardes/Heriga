from django.contrib import admin

# Register your models here.
from .models import UserGeneralInformation, UserJob, UserQualification, UserLanguage, UserPicture


class UserGeneralInformationAdmin(admin.ModelAdmin):	
	class Meta:
		model = UserGeneralInformation

admin.site.register(UserGeneralInformation, UserGeneralInformationAdmin)

class UserJobAdmin(admin.ModelAdmin):	
	class Meta:
		model = UserJob

admin.site.register(UserJob, UserJobAdmin)

class UserQualificationAdmin(admin.ModelAdmin):	
	class Meta:
		model = UserQualification

admin.site.register(UserQualification, UserQualificationAdmin)


class UserLanguageAdmin(admin.ModelAdmin):	
	class Meta:
		model = UserLanguage

admin.site.register(UserLanguage, UserLanguageAdmin)


class UserPictureAdmin(admin.ModelAdmin):	
	class Meta:
		model = UserPicture


admin.site.register(UserPicture, UserPictureAdmin)
