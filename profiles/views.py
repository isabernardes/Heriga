from django.shortcuts import render, RequestContext, Http404, render_to_response, get_object_or_404
from django.contrib.auth import get_user_model
from django.forms.models import modelformset_factory
from .models import *
from .forms import *

User = get_user_model()

# Create your views here.
def profile_detail(request, username):
		user = get_object_or_404(User, username=username)
		profile, created = UserGeneralInformation.objects.get_or_create(user=user)
		context = {'profile': profile, }

		return render(request, 'profiles/profile_detail.html', context)

def profile_update(request, username):
		user = request.user
		info = UserGeneralInformation.objects.get(user=user)
		jobs = UserJob.objects.filter(user=user)
		qualifications = UserQualification.objects.filter(user=user)
		languages = UserLanguage.objects.filter(user=user)
		pictures = UserPicture.objects.get(user=user)

		# Jobs Formset
		JobFormset = modelformset_factory(UserJob, form=UserJobForm, extra=1)
		formset_j = JobFormset(request.POST or None, queryset=jobs)

		# Qualifications Formset
		QualificationFormset = modelformset_factory(UserQualification, form=UserQualificationForm, extra =1)
		formset_q = QualificationFormset(request.POST or None, queryset=qualifications)

		# Languages Formset
		LanguageFormset = modelformset_factory(UserLanguage, form=UserLanguageForm, extra =1)
		formset_l = LanguageFormset(request.POST or None, queryset=languages)

		# Pictures Formset
		PictureFormset = modelformset_factory(UserPicture, form=UserPictureForm, extra =1)
		formset_p = PictureFormset(request.POST or None, queryset=pictures)

		info_form = UserGeneralInformationForm(request.POST or None, prefix='info', instance=info)
		#job_form = UserJobForm(request.POST or None, prefix='job', instance=job)
		#qualification_form = UserQualificationForm(request.POST or None, prefix='qualification', instance=qualification)
		#language_form = UserLanguageForm(request.POST or None, prefix='language', instance=language)
		#picture_form = UserPictureForm(request.POST or None, prefix='picture', instance=picture)

		if info_form.is_valid(): #and job_form.is_valid() and qualification_form.is_valid and language_form.is_valid and picture_form.is_valid():
			form1=info_form.save(commit=False)
			form1.save()
			#form2=job_form.save(commit=False)
			#form2.save()
			#form3=qualification_form.save(commit=False)
			#form3.save()
			#form4=language_form.save(commit=False)
			#form4.save()
			#form5=picture_form.save(commit=False)
			#form5.save()

		if formset_j.is_valid():
			pass

		if formset_q.is_valid():
			pass

		if formset_p.is_valid():
			pass

		if formset_l.is_valid():
			pass

		context = {
		"info_form": info_form,
		"formset_j": formset_j,
		"formset_q": formset_q,
		"formset_p": formset_p,
		"formset_l": formset_l,
	}

		return render(request, 'profiles/profile_forms.html', context)

	
