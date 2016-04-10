from django.contrib import admin


# Register your models here.
from .models import Communities

class CommunitiesModelAdmin(admin.ModelAdmin):	
	list_display = ["name", "description"]
	class Meta:
		model = Communities




admin.site.register(Communities, CommunitiesModelAdmin)