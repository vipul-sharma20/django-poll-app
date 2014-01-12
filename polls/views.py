from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("POLL INDEX ! :D ::TEST:: ")
def detail(request, poll_id):
    return HttpResponse("U are looking at poll %s " % poll_id)
def results(request, poll_id):
    return HttpResponse("U are looking at the results ! :D %s " % poll_id)
def vote(request, poll_id):
    return HttpResponse("U are voting on poll %s " % poll_id)

# Create your views here.
