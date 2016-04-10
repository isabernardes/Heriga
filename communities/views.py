from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .forms import CommunitiesForm
from .models import Communities

def communities_create(request):

	return render(request, "communities_form.html", {})

def communities_detail(request):
	instance = get_object_or_404(Communities, id=1)
	#Posts list of this community

	context = {
		"name": instance.name,
		"instance": instance
	}

	return render(request, "communities_detail.html",context)

def communities_list(request):
	queryset = Communities.objects.all()
	
	context = {
		"name": "List",
		"object_list": queryset
	}
	return render(request, "communities_list.html", context)


def communities_update(request):
	
	return render(request, "communities_form.html", {})



def communities_delete(request):
	
	return redirect("communities:list")