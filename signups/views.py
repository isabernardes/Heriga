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
	
