from django import forms
from .models import *

class UserGeneralInformationForm(forms.ModelForm):
    class Meta:
        model = UserGeneralInformation
        fields = "__all__" 


class UserJobForm(forms.ModelForm):
    class Meta:
        model = UserJob
        fields = "__all__" 
    
class UserQualificationForm(forms.ModelForm):
    class Meta:
        model = UserQualification
        fields = "__all__" 
     
class UserLanguageForm(forms.ModelForm):
    class Meta:
        model = UserLanguage
        fields = "__all__" 

class UserPictureForm(forms.ModelForm):
    class Meta:
        model = UserPicture
        fields = "__all__" 
      