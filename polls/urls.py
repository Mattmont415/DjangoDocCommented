
from django.urls import path
#From current directory, import the VIEWS file

from . import views

#use namespacing to prevent duplicates, for instance if another app had a 'detail' name
app_name = 'polls'

urlpatterns = [
  #/polls/
  path('', views.IndexView, name='index'),

  # #/polls/5, the 'name' value will be called by the {% url %} template tag
  # #Easier to modify pathname here, and not hardcoded all over documents
  # path('<int:question_id>/', views.detail, name='detail'),
  # #/polls/4/results/
  # path('<int:question_id>/results/', views.results, name='results'),
  # #/polls/5/vote/
  # path('<int:question_id>/vote/', views.vote, name='vote'),

  #GENERIC VIEWS - getting data from the database according to a parameter passed in URL
  #Loading a template, and returning a rendered template
  path('<int:pk>/', views.DetailView.as_view(), name='index'),
  path('<int:pk>/results/', view.ResultsView.as_view(), name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]