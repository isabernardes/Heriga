from django import forms
from .models import Communities

class CommunitiesForm(forms.ModelForm):
	class Meta:
		model = Communities
		fields = [
			"name",
			"description",
			"image",
		]