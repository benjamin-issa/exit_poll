from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from random import randrange
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/voters/instructions/')
    return render (request, 'login.html')

def authenticate(request):
    usern = request.POST.get('Username', '')
    passw = request.POST.get('Password', '')
    user = auth(username = usern, password = passw)      
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/voters/instructions')
    else:
        return HttpResponseRedirect('/account/loginfail')

def loginfail(request):
    return render (request, 'loginfail.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/account/login')

@login_required
def accountdetail(request):
    return render (request, 'accountdetail.html')

@login_required
def changepassword(request):
    pass1 = request.POST.get('password1', '')
    pass2 = request.POST.get('password2', '')
    if pass1 == pass2 and pass1 != "":
        request.user.set_password(pass1)
        request.user.save()
        auth_logout(request)
        return HttpResponseRedirect('/account/login')
    else:
        return HttpResponseRedirect('/account/changefail')

@login_required    
def changefail(request):
    return render (request, 'changefail.html')
