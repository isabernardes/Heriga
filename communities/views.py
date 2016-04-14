from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .forms import CommunitiesForm
from .models import Communities
from posts.models import Post

def communities_create(request):

	return render(request, "communities_form.html", {})

def communities_detail(request):
	#instance = get_object_or_404(Communities, id=1)
	
	#today = timezone.now().date()
	queryset_list = Post.objects.filter(community_id=1)


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
		"object_list": queryset_list,
		"title": "List",
	#	"today": today,
	#	"page_request_var": page_request_var
	}
	return render(request, "post_list.html", context)



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


def communities_update(request):
	
	return render(request, "communities_form.html", {})



def communities_delete(request):
	
	return redirect("communities:list")