from urllib import quote_plus
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
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
from django.views.decorators.http import require_POST
from django.views.generic import View
import datetime
from profiles.models import UserJob
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.views.generic import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

User = get_user_model()

def home(request):
	queryset_one = Post.objects.all().order_by("-timestamp")[:1]
	queryset_two = Communities.objects.all().order_by("-timestamp")[:3]
	context = {
		"queryset_story": queryset_one,
		"queryset_community":queryset_two
	}

	return render (request, "home.html", context)

def aboutus(request):
	return render (request, "aboutus.html")

@login_required
def post_create(request):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
	context = {
		"form": form,
	}
	return render(request, "stories/post_form.html", context)


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

	return render(request, "stories/post_detail.html", context)


class PostLikeToggle(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		slug = self.kwargs.get("slug")
		print(slug)
		obj = get_object_or_404(Post, slug=slug)
		url_ = obj.get_absolute_url()
		user = self.request.user
		if user.is_authenticated():
			if user in obj.likes.all():
				obj.likes.remove(user)
			else:
				obj.likes.add(user)
		return url_


class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        # slug = self.kwargs.get("slug")
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)

def tags(request, tag):
	posts = Post.objects.filter(tags__name=tag)
	name = Post.objects.all(),
	context={
            'posts': posts,
            'tags':tag,
            'name': tag,
        } 
 
	return render(request, "stories/tags_list.html", context)


def post_list(request, slug=None):
	author = User.objects.all()
	today = timezone.now().date()
	queryset_list = Post.objects.active()#.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
		queryset_list.user = request.user

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
		"author": author,
		"title": "List",
		"today": today,
	}
	return render(request, "stories/post_list.html", context)

def user(request, username):
	user = User.objects.all()
	context = {
		
		"user": user,
		
	}
	return render(request, "stories/post_list.html", context)



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

	return render(request, "stories/post_form.html", context)
	

def post_delete(request, slug=None):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
	instance = get_object_or_404(Post, slug =slug)
	messages.success(request, "Successfully Deleted")
	instance.delete()
	return redirect("posts:list")

def post_profile(request):
	queryset_list = Post.objects.all()

	context = {
		"object_list": queryset_list,
	}

	return render(request, "profiles/profile_list.html", context)






