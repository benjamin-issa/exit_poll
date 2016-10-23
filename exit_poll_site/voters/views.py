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
        if voter.which_call() == 7:
            voter.call_seven_phone = phone
            voter.call_seven = True
            voter.call_seven_time = datetime.now()
            voter.call_seven_user = request.user.get_full_name()
            voter.call_seven_outcome = result
        if voter.which_call() == 6:
            voter.call_six_phone = phone
            voter.call_six = True
            voter.call_six_time = datetime.now()
            voter.call_six_user = request.user.get_full_name()
            voter.call_six_outcome = result
        if voter.which_call() == 5:
            voter.call_five_phone = phone
            voter.call_five = True
            voter.call_five_time = datetime.now()
            voter.call_five_user = request.user.get_full_name()
            voter.call_five_outcome = result
        if voter.which_call() == 4:
            voter.call_four_phone = phone
            voter.call_four = True
            voter.call_four_time = datetime.now()
            voter.call_four_user = request.user.get_full_name()
            voter.call_four_outcome = result
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
    #all_voters = Voter.objects.all()
    #For call one
    call_one_voters = Voter.objects.filter(call_one=False)
    valid_call_one_voters = []
    for voter in call_one_voters:
        if (voter.is_callable()):
             valid_call_one_voters.append(voter.pk)
    if len(valid_call_one_voters) != 0:
        random_index = randrange(0,len(valid_call_one_voters))
        v = Voter.objects.get(pk=valid_call_one_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(valid_call_one_voters[random_index]))
    
    #For call two
    call_two_voters = Voter.objects.filter(call_two=False)
    valid_call_two_voters = []
    for voter in call_two_voters:
        if (voter.is_callable()):
             valid_call_two_voters.append(voter.pk)
    if len(valid_call_two_voters) != 0:
        random_index = randrange(0,len(valid_call_two_voters))
        v = Voter.objects.get(pk=valid_call_two_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(valid_call_two_voters[random_index]))
    
    
    #For call three
    call_three_voters = Voter.objects.filter(call_three=False)
    valid_call_three_voters = []
    for voter in call_three_voters:
        if (voter.is_callable()):
             valid_call_three_voters.append(voter.pk)
    if len(valid_call_three_voters) != 0:
        random_index = randrange(0,len(valid_call_three_voters))
        v = Voter.objects.get(pk=valid_call_three_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(valid_call_three_voters[random_index]))
    
    #For call four
    call_four_voters = Voter.objects.filter(call_four=False)
    valid_call_four_voters = []
    for voter in call_four_voters:
        if (voter.is_callable()):
             valid_call_four_voters.append(voter.pk)
    if len(valid_call_four_voters) != 0:
        random_index = randrange(0,len(valid_call_four_voters))
        v = Voter.objects.get(pk=valid_call_four_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(valid_call_four_voters[random_index]))
    
    #For call five
    call_five_voters = Voter.objects.filter(call_five=False)
    valid_call_five_voters = []
    for voter in call_five_voters:
        if (voter.is_callable()):
             valid_call_five_voters.append(voter.pk)
    if len(valid_call_five_voters) != 0:
        random_index = randrange(0,len(valid_call_five_voters))
        v = Voter.objects.get(pk=valid_call_five_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(valid_call_five_voters[random_index]))
    
    #For call six
    call_six_voters = Voter.objects.filter(call_six=False)
    valid_call_six_voters = []
    for voter in call_six_voters:
        if (voter.is_callable()):
             valid_call_six_voters.append(voter.pk)
    if len(valid_call_six_voters) != 0:
        random_index = randrange(0,len(valid_call_six_voters))
        v = Voter.objects.get(pk=valid_call_six_voters[random_index])
        v.last_display_time = datetime.now()
        v.save()
        return HttpResponseRedirect ('/voters/' + str(valid_call_six_voters[random_index]))
    
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
        voter.last_display_time = datetime.now()
        return HttpResponseRedirect('/voters/' + str(voter.pk))
    else:
        return render(request, 'voters/lookuperror.html')
    
@login_required
def lookuperror(request):
    return render(request, 'voters/lookuperror.html')
