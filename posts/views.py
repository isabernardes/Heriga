from urllib import quote_plus
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

# Create your views here.

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form =PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug = None):
	instance =get_object_or_404(Post, slug =slug)
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance":instance,
		"share_string": share_string,
	}

	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all().order_by("-timestamp")
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request, "post_list.html", context)

def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id =slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance":instance,
		"form":form,
	}

	return render(request, "post_form.html", context)
	

def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug =slug)
	messages.success(request, "Successfully Deleted")
	instance.delete()
	return redirect("posts:list")