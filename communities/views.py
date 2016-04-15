from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .forms import CommunitiesForm
from .models import Communities
from posts.models import Post
from django.contrib import messages

def communities_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form =CommunitiesForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Created")
	context = {
		"form": form,
	}
	return render(request, "communities_form.html", context)


def communities_detail(request, id=None):
	instance = get_object_or_404(Communities, id=id)
	
	#today = timezone.now().date()
	queryset = Post.objects.filter(community_id=id)


	#query = request.GET.get("q")
	#if query:
	#	queryset_list = queryset_list.filter(
	#			Q(title__icontains=query)|
	#			Q(content__icontains=query)|
	#			Q(user__first_name__icontains=query) |
	#			Q(user__last_name__icontains=query)
	#			).distinct()
	#paginator = Paginator(queryset_list, 10) 
	#page_request_var = "page"
	#page = request.GET.get(page_request_var)
	#try:
	#	queryset = paginator.page(page)
	#except PageNotAnInteger:
	#	If page is not an integer, deliver first page.
	#	queryset = paginator.page(1)
	#except EmptyPage:
	#	If page is out of range (e.g. 9999), deliver last page of results.
	#	queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"instance": instance,
	#	"today": today,
	#	"page_request_var": page_request_var
	}
	return render(request, "communities_detail.html", context)



	#
	#Posts list of this community
	#queryset_postlist = Post.objects.filter(community_id=1)

	#context = {
#		"name": instance.name,
	#	"instance": instance,
	#	"queryset_postlist": queryset_postlist,
	#}

	#return render(request, "communities_detail.html",context)

def communities_list(request):
	queryset = Communities.objects.all()
	
	context = {
		"name": "List",
		"object_list": queryset
	}
	return render(request, "communities_list.html", context)


def communities_update(request, id =None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id =id)
	form = CommunitiesForm(request.POST or None, request.FILES or None, instance=instance)
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

	return render(request, "communities_form.html", context)


def communities_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id =id)
	messages.success(request, "Successfully Deleted")
	instance.delete()
	return redirect("communities:list")
	
	return redirect("communities:list")