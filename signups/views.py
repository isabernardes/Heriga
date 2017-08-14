from django.shortcuts import render
#from .models import SignUp
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from signups.forms import *
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
#def register_user(request):
    #if request.method == 'POST':
        #form = MyRegistrationForm(request.POST)     # create form object
        #if form.is_valid():
            #form.save()
            #return HttpResponseRedirect('/accounts/register_success')
    #args = {}
    #args.update(csrf(request))
    #args['form'] = MyRegistrationForm()
    #print args
    #return render(request, 'signup.html', args)


def home(request):
    title = 'Sign up now'
    form = UserRegistrationForm(request.POST or None)
    context = {
        "title": title,
        "form":form
    }

    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }

    if request.user.is_authenticated():
        queryset_one = Post.objects.all().order_by("-timestamp")[:1]
        queryset_two = Communities.objects.all().order_by("-timestamp")[:3]
    
        context = {
            "queryset_story": queryset_one,
            "queryset_community":queryset_two
        }

    return render (request, "home.html", context)

def contactus(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youotheremail@email.com']
        contact_message = "%s: %s via %s"%( 
                form_full_name, 
                form_message, 
                form_email)
        some_html_message = """
        <h1>hello</h1>
        """
        send_mail(subject, 
                contact_message, 
                from_email, 
                to_email, 
                html_message=some_html_message,
                fail_silently=True)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }

    return render (request, "contactus.html")

    
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = UserRegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/signup.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
	
