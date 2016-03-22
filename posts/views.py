from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

# Create your views here.

def posts_create(request):

	return HttpResponse("<h1>Create</h1>")

def posts_detail(request):
	context = {
		"title": "Detail"
	}

	return render(request, "index", context)

def posts_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request, "index.html", context)

def posts_update(request):

	return HttpResponse("<h1>Update</h1>")

def posts_delete(request):

	return HttpResponse("<h1>Delete</h1>")