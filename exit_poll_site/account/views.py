from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from random import randrange

# Create your views here.

def login(request):
    return render (request, 'login.html')