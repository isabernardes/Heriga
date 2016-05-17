from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .forms import CommunitiesForm
from .models import Communities
from posts.models import Post
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def communities_create(request):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	form =CommunitiesForm(request.POST or None, request.FILES or None)
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
	return render(request, "communities/communities_form.html", context)


def communities_detail(request, slug=None):
	instance = get_object_or_404(Communities, slug=slug)
	queryset = Post.objects.filter(community__slug=slug)
	context = {
		"object_list": queryset,
		"instance": instance,
	}
	return render(request, "stories/post_list.html", context)


def communities_list(request):
	queryset = Communities.objects.all()
	query = request.GET.get("q")
	if query:
		queryset = queryset= queryset.filter(
				Q(name__icontains=query)|
				Q(description__icontains=query)
				).distinct()
	
	context = {
		"name": "List",
		"object_list": queryset
	}
	return render(request, "communities/communities_list.html", context)

@login_required
def communities_update(request, slug =None):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	instance = get_object_or_404(Communities, slug =slug)
	form = CommunitiesForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.name,
		"instance":instance,
		"form":form,
	}

	return render(request, "communities/communities_form.html", context)

@login_required
def communities_delete(request, slug=None):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	instance = get_object_or_404(Communities, slug =slug)
	messages.success(request, "Successfully Deleted")
	instance.delete()
	return redirect("communities:communities_list")
	
