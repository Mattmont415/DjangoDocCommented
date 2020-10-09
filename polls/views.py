#Common to get an object or raise 404, django's shortcut
from django.shortcuts import render, get_object_or_404
#Http404 needs to be imported to handle 404 errorss
from django.http import HttpResponse, Http404
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
  # template = loader.get_template('polls/index.html')
  # context = { #Loads template and PASSES it a context: a dict mapping template variable
  # #names to python objects
  #   'latest_question_list': latest_question_list
  # }
  # return HttpResponse(template.render(context, request))
  #The above lines rewritten as...
  context = {'latest_question_list': latest_question_list}
  #The render function takes the REQUEST object, a template name, and dict, it 
  #returns an HTTPResponse object of the given template rendered WITh that context
  return render(request, 'polls/index.html', context)

#Called to object from address bar
#detail(request=<HttpRequest object>, question_id=34)
def detail(request, question_id):
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   #Raises 404 exception if a question with requested ID does not exist
  #   raise Http404('Question does not exist')
  # return render(request, 'polls/detail.html', {'question': question})
  #this can be rewritten as...
  question = get_object_or_404(Question, pk=question_id) #raise 404 if does not exist
  return render(request, 'polls/detail,html', {'question': question})

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
