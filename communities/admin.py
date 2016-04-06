from django.contrib import admin


# Register your models here.
from .models import Communities

class CommunitiesModelAdmin(admin.ModelAdmin):	
	list_display = ["title", "content"]
	class Meta:
		model = Communities




admin.site.register(Communities, CommunitiesModelAdmin)