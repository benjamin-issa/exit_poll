from django.shortcuts import render, get_object_or_404
from datetime import datetime   
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from random import randrange
from django.contrib.auth.decorators import login_required
from .models import Voter, Phone

@login_required
def index(request):
    voter_list = Voter.objects.order_by('-respondent_id')[:30000]
    output = ', '.join([v.name for v in voter_list])
    template = loader.get_template('voters/index.html')
    context = {
        'voter_list': voter_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def detail(request, respondent_id):
    try:
        voter = Voter.objects.get(pk=respondent_id)
    except Voter.DoesNotExist:
        raise Http404("No respondent with that respondent id was found.")
    return render(request, 'voters/detail.html', {'voter': voter})

@login_required
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
        phone.user_marking_invalid = request.user.get_full_name()
        phone.save()
        return HttpResponseRedirect('/voters/result_instructions')
    #If the call was completed
    if result == "TS" or result == "NH" or result == "LV" or result == "CB" or result == "SD" or result == "HD":
        phone = voter.get_phone_number()
        if voter.which_call() == 3:
            voter.call_three_phone = phone
            voter.call_three = True
            voter.call_three_time = datetime.now()
            voter.call_three_user = request.user.get_full_name()
            voter.call_three_outcome = result
        if voter.which_call() == 2:
            voter.call_two_phone = phone
            voter.call_two = True
            voter.call_two_time = datetime.now()
            voter.call_two_user = request.user.get_full_name()
            voter.call_two_outcome = result
        if voter.which_call() == 1:
           voter.call_one_phone = phone
           voter.call_one = True
           voter.call_one_time = datetime.now()
           voter.call_one_user = request.user.get_full_name()
           voter.call_one_outcome = result
        voter.save()
        return HttpResponseRedirect('/voters/result_instructions')
    return HttpResponse(result)

@login_required
def random(request):
    all_voters = Voter.objects.all()
    #For call one
    call_one_voters = []
    for voter in all_voters:
        if (voter.which_call() == 1 and voter.is_callable()):
            call_one_voters.append(voter.pk)
    if len(call_one_voters) != 0:
        random_index = randrange(0,len(call_one_voters))
        v = Voter.objects.get(pk=call_one_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(call_one_voters[random_index]))
    #For call two
    call_two_voters = []
    for voter in all_voters:
        if (voter.which_call() == 2 and voter.is_callable()):
            call_two_voters.append(voter.pk)
    if len(call_two_voters) != 0:
        random_index = randrange(0,len(call_two_voters))
        v = Voter.objects.get(pk=call_two_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(call_two_voters[random_index]))
    #For call three
    call_three_voters = []
    for voter in all_voters:
        if (voter.which_call() == 3 and voter.is_callable()):
            call_three_voters.append(voter.pk)
    if len(call_three_voters) != 0:
        random_index = randrange(0,len(call_three_voters))
        v = Voter.objects.get(pk=call_three_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(call_two_voters[random_index]))
    return render(request, 'voters/error.html')

@login_required
def result_page(request):
    return render(request, 'voters/result_page.html')

@login_required
def instructions(request):
    return render(request, 'voters/instructions.html')

@login_required
def lookup(request):
    return render(request, 'voters/lookup.html')

@login_required
def processvl(request):
    voters = Voter.objects.all()
    vid = request.POST.get('voter_id', '')
    if voters.filter(respondent_id=vid).exists():
        voter = Voter.objects.get(respondent_id=vid)
        return HttpResponseRedirect('/voters/' + str(voter.pk))
    else:
        return render(request, 'voters/lookuperror.html')
    
@login_required
def lookuperror(request):
    return render(request, 'voters/lookuperror.html')
