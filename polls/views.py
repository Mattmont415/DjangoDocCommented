#Common to get an object or raise 404, django's shortcut
from django.shortcuts import render, get_object_or_404
#Http404 needs to be imported to handle 404 errorss
from django.http import HttpResponse, Http404, HttpResponseRedirect
#this is for loading up a template :)
from django.template import loader
from django.urls import reverse
#need to import generic to work with django's generic views
from django.views import generic

#Import each model that will be used in the views
from .models import Choice, Question

#A view is a type of Web page in Django app that serves a specific function with template
#Web pages and other content are delivered by views
#To get from a URL to a view, Django uses URLconfs, a URLconf maps URL patterns to views

#Each view is responsible for doing one of two things, returning HttpResponse object
#OR raising an exception

# Create your views here.
#Each generic view needs to know what model it will be acting upon
#ListView - Display a list of objects!
class IndexView(generic.ListView):
  template+name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions."""
    return Question.objects.order_by('-pub_date')[:5]
#The detailview expects the primary key value captured from the URL, why we switched
#question_id for PK
#Detail view - Display a detail page for a particular type of object
class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    #request.POST dictionary-like object that lets you access submitted data
    #...POST['choice'] returns the ID of the selected choice as string (always string)
    #Choice is from the form name="choice" in detail.html
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  #raises error if Choice was not provided in POST data
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't make a CHOICE!",
    })
  else:
    #Increments the choice count
    selected_choice.votes += 1
    selected_choice.save()
    #Always return HttpResponseRedirect after DEALING WITH POST DATA
    #Data will not be posted twice this way!
    #This takes a single argument, the URL the user will be redirected to
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    #Reverse is given the name of the view we want to pass control to
    #Reverse will return a string like '/polls/3/results/'