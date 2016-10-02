from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Voter

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
    return HttpResponse("Placeholder")
