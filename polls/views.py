from django.shortcuts import render
from django.http import HttpResponse
#this is for loading up a template :)
from django.template import loader

from .models import Question

#A view is a type of Web page in Django app that serves a specific function with template
#Web pages and other content are delivered by views
#To get from a URL to a view, Django uses URLconfs, a URLconf maps URL patterns to views

#Each view is responsible for doing one of two things, returning HttpResponse object
#OR raising an exception

# Create your views here.

#This will display the latest 5 poll questions, separated by commas, according to publication date
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = { #Loads tempalte and PASSES it a context: a dict mapping template variable
  #names to python objects
    'latest_question_list': latest_question_list
  }
  return HttpResponse(template.render(context, request))

#Called to object from address bar
#detail(request=<HttpRequest object>, question_id=34)
def detail(request, question_id):
  return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
