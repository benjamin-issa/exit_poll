from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from random import randrange
from django.contrib.auth.decorators import login_required
from voters.models import Voter, Phone

@login_required
def index(request):
    return render(request, 'index.html')
