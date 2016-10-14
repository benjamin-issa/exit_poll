from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from random import randrange
from django.contrib.auth.decorators import login_required
from voters.models import Voter, Phone

@login_required
def index(request):
    voters = Voter.objects.all()
    voters_waveone = Voter.objects.filter(respondent_wave = "W1")
    number_taken_survey = "12"
    #for voter in voters:
    #    if voter.took_survey() == True:
    #        number_taken_survey = number_taken_survey + 1
    return render(request, 'index.html', {'voters': voters}, {'number_taken_survey': number_taken_survey})