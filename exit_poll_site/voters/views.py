from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Voter, Phone

def index(request):
    voter_list = Voter.objects.order_by('-respondent_id')[:30000]
    output = ', '.join([v.name for v in voter_list])
    template = loader.get_template('voters/index.html')
    context = {
        'voter_list': voter_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, respondent_id):
    try:
        voter = Voter.objects.get(pk=respondent_id)
    except Voter.DoesNotExist:
        raise Http404("No respondent with that respondent id was found.")
    return render(request, 'voters/detail.html', {'voter': voter})

def result(request, voter_id):
    voter = get_object_or_404(Voter, pk=voter_id)
    try:
        result = request.POST['result']
    except:
        return HttpResponseRedirect('/voters/' + voter_id)
    #If phone number was disconnected.
    if result == "DC":
        phone = voter.get_phone_number()
        phone.valid = False
        phone.save()
        return HttpResponse("processed.")
    #If voter took the survey
    if result == "TS" or result == "NH" or result == "LV" or result == "CB" or result == "SD" or result == "HD":
        phone = voter.get_phone_number()
        if voter.which_call() == 3:
            voter.call_three_phone = phone
            voter.call_three = True
            voter.call_three_time = datetime.now()
            voter.call_three_user = "placeholder"
            voter.call_three_outcome = result
        if voter.which_call() == 2:
            voter.call_two_phone = phone
            voter.call_two = True
            voter.call_two_time = datetime.now()
            voter.call_two_user = "placeholder"
            voter.call_two_outcome = result
        if voter.which_call() == 1:
           voter.call_one_phone = phone
           voter.call_one = True
           voter.call_one_time = datetime.now()
           voter.call_one_user = "placeholder"
           voter.call_one_outcome = result
        voter.save()
        return HttpResponse("Processed.")
    return HttpResponse(result)
