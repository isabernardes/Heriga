from django.contrib import messages
from django.shortcuts import render, RequestContext, render_to_response, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import get_user_model
from django.forms.models import modelformset_factory
from profiles.models import Profile
from .forms import *
from signups import *
from posts.views import *
from posts.models import Post
from communities.models import Communities
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


User = get_user_model()


@login_required
def profile_view(request, username):
		user = get_object_or_404(User, username=username)
		userprofile = User.objects.get(username=username)
		profile, created = Profile.objects.get_or_create(user=user)
		#posts = Post.objects.filter(user=user)
		
		context = {
			'profile': profile, 
			'userprofile': userprofile,
			#'posts': posts
		}
		return render(request, 'profiles/profile_view.html', context)

@login_required
def profile_update(request, username):
		user = request.user.profile
		profile = Profile.objects.all()
		info = Profile.objects.get(user=request.user)
		
		if profile != request.user:
			return (request, 'profiles/profile_view.html')
		

		else:
			form = ProfileForm(request.POST or None, instance=info)
			if form.is_valid():
		 		instance=form.save(commit=False)
		 		instance.user = request.user
		 		instance.save()
		 		form.save_m2m()
		 		messages.success(request, "Successfully Created")
		 		return HttpResponseRedirect(instance.get_absolute_url())
		 	else:
		 		messages.error(request, "Not Successfully Created")
		 				
		 	context = {
		 		"form": form,
		 	}
		 	return render(request, 'profiles/profile_forms.html', context)

		

	

	

		

		








	
