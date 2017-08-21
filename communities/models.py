from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#from posts.models import Post


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

#class CommunitiesManager(models.Manager):
#	def active(self, *args, **kwargs):
#		return super(CommunitiesManager, self).filter(community__slug=slug)



class CommunitiesManager(models.Manager):
    #def all(self):
     #   qs = super(CommunitiesManager, self).filter(parent=None)
      #  return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommunitiesManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs


class Communities(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	name = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
	object_id      = models.PositiveIntegerField(null=True, blank=True)
	content_object = GenericForeignKey('content_type', 'object_id')
	parent         = models.ForeignKey("self", null=True, blank=True)
		

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("communities:detail", kwargs={"slug": self.slug})

	#objects = CommunitiesManager()


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Communities.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Communities)


  