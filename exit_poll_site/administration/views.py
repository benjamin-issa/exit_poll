from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from random import randrange
from django.contrib.auth.decorators import login_required
from voters.models import Voter, Phone
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def index(request):
    voters = Voter.objects.all()
    voters_waveone = Voter.objects.filter(respondent_wave__exact = "W1")
    voters_wavetwo = Voter.objects.filter(respondent_wave__exact = "W2")
    voters_wavethree = Voter.objects.filter(respondent_wave__exact = "W3")
    voters_wavefour = Voter.objects.filter(respondent_wave__exact = "W4")
    voters_wavefive = Voter.objects.filter(respondent_wave__exact = "W5")
    voters_took_survey = Voter.objects.filter(Q(call_one_outcome = "TS") | Q (call_two_outcome = "TS") |
                                              Q(call_three_outcome = "TS") | Q (call_four_outcome = "TS") |
                                              Q(call_five_outcome = "TS") | Q (call_six_outcome = "TS") |
                                              Q(call_seven_outcome = "TS") | Q(done_online_survey = True))
    voters_took_survey_phone = Voter.objects.filter(Q(call_one_outcome = "TS") | Q (call_two_outcome = "TS") |
                                              Q(call_three_outcome = "TS") | Q (call_four_outcome = "TS") |
                                              Q(call_five_outcome = "TS") | Q (call_six_outcome = "TS") |
                                              Q(call_seven_outcome = "TS"))
    voters_took_survey_internet = Voter.objects.filter(done_online_survey = True)
    response_rate = (voters_took_survey.count() / float(voters.count()) * 100)
    
    
    w1_voters_took_survey = voters_took_survey.filter(respondent_wave = "W1")
    w1_response_rate = (w1_voters_took_survey.count() / float(voters_waveone.count()) * 100)
    w1_phone = voters_took_survey_phone.filter(respondent_wave = "W1")
    w1_internet = voters_took_survey_internet.filter(respondent_wave = "W1")
    
    w2_voters_took_survey = voters_took_survey.filter(respondent_wave = "W2")
    w2_response_rate = (w2_voters_took_survey.count() / float(voters_wavetwo.count()) * 100)
    w2_phone = voters_took_survey_phone.filter(respondent_wave = "W2")
    w2_internet = voters_took_survey_internet.filter(respondent_wave = "W2")
    
    w3_voters_took_survey = voters_took_survey.filter(respondent_wave = "W3")
    w3_response_rate = (w3_voters_took_survey.count() / float(voters_wavethree.count()) * 100)
    w3_phone = voters_took_survey_phone.filter(respondent_wave = "W3")
    w3_internet = voters_took_survey_internet.filter(respondent_wave = "W3")
    
    w4_voters_took_survey = voters_took_survey.filter(respondent_wave = "W4")
    w4_response_rate = (w4_voters_took_survey.count() / float(voters_wavefour.count()) * 100)
    w4_phone = voters_took_survey_phone.filter(respondent_wave = "W4")
    w4_internet = voters_took_survey_internet.filter(respondent_wave = "W4")
    
    w5_voters_took_survey = voters_took_survey.filter(respondent_wave = "W5")
    w5_response_rate = (w5_voters_took_survey.count() / float(voters_wavefive.count()) * 100)
    w5_phone = voters_took_survey_phone.filter(respondent_wave = "W5")
    w5_internet = voters_took_survey_internet.filter(respondent_wave = "W5")
    
    #for voter in voters:
    #    if voter.took_survey() == True:
    #        number_taken_survey = number_taken_survey + 1
    return render(request, 'index.html', {'voters_waveone': voters_waveone, 'voters': voters, 'voters_wavetwo': voters_wavetwo,
                                          'voters_wavethree': voters_wavethree, 'voters_wavefour': voters_wavefour, 'voters_wavefive': voters_wavefive,
                                          'voters_took_survey': voters_took_survey, 'response_rate': response_rate,
                                          'w1_voters_took_survey': w1_voters_took_survey, 'w1_response_rate': w1_response_rate,
                                          'w1_phone': w1_phone, 'w1_internet': w1_internet,
                                          'w2_voters_took_survey': w2_voters_took_survey, 'w2_response_rate': w2_response_rate,
                                          'w2_phone': w2_phone, 'w2_internet': w2_internet,
                                          'w3_voters_took_survey': w3_voters_took_survey, 'w3_response_rate': w3_response_rate,
                                          'w3_phone': w3_phone, 'w3_internet': w3_internet,
                                          'w4_voters_took_survey': w4_voters_took_survey, 'w4_response_rate': w4_response_rate,
                                          'w4_phone': w4_phone, 'w4_internet': w4_internet,
                                          'w5_voters_took_survey': w5_voters_took_survey, 'w5_response_rate': w5_response_rate,
                                          'w5_phone': w5_phone, 'w5_internet': w5_internet,
                                          })