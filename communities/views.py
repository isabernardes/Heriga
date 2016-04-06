from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.

from django.http import HttpResponse


from .forms import CommunitiesForm
from .models import Communities

def communities_create(request):

	return render(request, "communities_form.html", {})

def communities_detail(request, id=None):

	return render(request, "communities_detail.html",{})

def communities_list(request):

	return render(request, "communities_list.html", {})


def communities_update(request, id=None):
	
	return render(request, "communities_form.html", {})



def communities_delete(request, id=None):
	
	return redirect("communities:list")