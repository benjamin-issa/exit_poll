from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from random import randrange
from django.contrib.auth import authenticate as auth
import django.middleware.csrf

def login(request):
    return render (request, 'login.html')

def authenticate(request):
    usern = request.POST.get('username', '')
    passw = request.POST.get('password', '')
    return HttpResponse("Username: " + usern + "     Password: " + passw)
    user = auth(username = usern, password = passw)      
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/voters/instructions')
    else:
        return HttpResponseRedirect('/account/loginfail')

def loginfail(request):
    return render (request, 'loginfail.html')

