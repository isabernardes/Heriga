from __future__ import unicode_literals

from django.apps import AppConfig

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


class SignupsConfig(AppConfig):
    name = 'signups'
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/");
    else:
        form = UserCreationForm()
    return render(request, "signup.html",{
        'form':form,
    })
