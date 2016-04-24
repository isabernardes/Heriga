from urllib import quote_plus
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm
from .models import Post
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from communities.models import Communities
from taggit.models import Tag


def home(request):
	queryset_one = Post.objects.all().order_by("-timestamp")[:1]
	#queryset_two = Communities.objects.all().order_by("-timestamp")[:3]
	context = {
		"object_list": queryset_one,
		#"object_list":queryset_two
	}

	return render (request, "home.html", context)

def aboutus(request):
	return render (request, "aboutus.html")

@login_required
def post_create(request):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	form =PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form.save_m2m()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

@login_required
def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	#if instance.publish > timezone.now().date() or instance.draft:
		#if not request.user.is_staff or not request.user.is_superuser:
		#	raise Http404
	share_string = quote_plus(instance.content)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}

	#FORM SAVE
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)

		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	comments = instance.comments
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form":form,
		"tags": tags
	}

	extra_context={
            'objects':Post.objects.all(),
        } 

	return render(request, "post_detail.html", context)

def tags(request, tag):
	queryset_tags = Post.objects.filter(tags__name__in=[tag])
	context={
            'posts': queryset_tags,
        } 
	return render(request, "post_detail.html", context)


def tags_list(request, tag_slug=None):
	tags_list = Post.objects.filter(published='True', tags__name__in=[slug])
	pages = Paginator(posts, 5)
	returned_page = pages.page(selected_page)
	context= {
		'page_obj': returned_page,
		'tags_list':tags_list
	}
	return render(request, "tags_list.html", context)



def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()#.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()

	context = {
		"object_list": queryset_list,
		"title": "List",
		"today": today,
	}
	return render(request, "post_list.html", context)

@login_required
def post_update(request, slug=None):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	instance = get_object_or_404(Post, slug =slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form.save_m2m()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())			

	context = {
		"title": instance.title,
		"instance":instance,
		"form":form,
		"tags":tags
	}

	

	return render(request, "post_form.html", context)
	

def post_delete(request, slug=None):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	instance = get_object_or_404(Post, slug =slug)
	messages.success(request, "Successfully Deleted")
	instance.delete()
	return redirect("posts:list")
