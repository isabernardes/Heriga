from django.shortcuts import render, RequestContext, Http404, render_to_response, get_object_or_404
from django.contrib.auth import get_user_model
from django.forms.models import modelformset_factory
from .models import *
from .forms import *
from signups import *
from posts.views import *
from posts.models import Post
from communities.models import Communities
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


User = get_user_model()


#def home(request):
#	title = 'Sign up now'
#	form = UserRegistrationForm(request.POST or None)
#	context = {
#		"title": title,
#		"form":form
#	}
#
#	if form.is_valid():
#		instance = form.save(commit=False)
#
#		full_name = form.cleaned_data.get("full_name")
#		if not full_name:
#			full_name = "New full name"
#		instance.full_name = full_name
#		instance.save()
#		context = {
#			"title": "Thank you"
#		}
#
#	if request.user.is_authenticated():
#		queryset_one = Post.objects.all().order_by("-timestamp")[:1]
#		queryset_two = Communities.objects.all().order_by("-timestamp")[:3]
#	
#		context = {
#			"queryset_story": queryset_one,
#			"queryset_community":queryset_two
#		}
#
#	return render (request, "home.html", context)

#def aboutus(request):
#	return render (request, "aboutus.html")








@login_required
def profile_detail(request, username):
		user = get_object_or_404(User, username=username)
		user = request.user
		profile, created = UserGeneralInformation.objects.get_or_create(user=user)
		
		context = {
			'profile': profile, 
		}
		return render(request, 'profiles/profile_detail.html', context)


def profile_update(request, username):
		user = request.user
		info = UserGeneralInformation.objects.get(user=user)
		jobs = UserJob.objects.filter(user=user)
		qualifications = UserQualification.objects.filter(user=user)
		languages = UserLanguage.objects.filter(user=user)
		#pictures, created = UserPicture.objects.get_or_create(user=user)

		# Info Formset
		info_form = UserGeneralInformationForm(request.POST or None, prefix='info', instance=info)

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
		#PictureFormset = modelformset_factory(UserPicture, form=UserPictureForm, extra =1)
		#formset_p = PictureFormset(request.POST or None, queryset=pictures)

		
		#Save Formset
		if info_form.is_valid(): 
			form1=info_form.save(commit=False)
			form1.save()
			
		if formset_j.is_valid():
			pass

		if formset_q.is_valid():
			pass

		#if formset_p.is_valid():
			#pass

		if formset_l.is_valid():
			pass

		context = {
		"info_form": info_form,
		"formset_j": formset_j,
		"formset_q": formset_q,
		#"formset_p": formset_p,
		"formset_l": formset_l,
	}

		return render(request, 'profiles/profile_forms.html', context)

	

		

	

		

		








	
