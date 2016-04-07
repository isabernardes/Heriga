from django.shortcuts import render
from .models import SignUp
from django.core.urlresolvers import reverse
from django.http import HttpResponse

# Create your views here.
def SignUp (request):
	return render(request, "signup.html", {})