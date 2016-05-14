from django.shortcuts import render, RequestContext, Http404, render_to_response, get_object_or_404
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

# Create your views here.
def profile_view(request, username):
		user = get_object_or_404(User, username=username)
		profile, created = UserGeneralInformation.objects.get_or_create(user=user)
		context = {'profile': profile, }

		return render(request, 'profile.html', context)
