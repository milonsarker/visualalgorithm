from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template('sortingAlgorithm/index.html')
    context = {
            'Name': 'Corleone',
            }
    return HttpResponse(template.render(context,request))

def sortingAlgo(request, algoName):
    return HttpResponse("<h2>This "+str(algoName)+" buddy... :) </h2>")
