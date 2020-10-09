
from django.urls import path
#From current directory, import the VIEWS file

from . import views

#use namespacing to prevent duplicates, for instance if another app had a 'detail' name
app_name = 'polls'

urlpatterns = [
  #/polls/
  path('', views.index, name='index'),

  #/polls/5, the 'name' value will be called by the {% url %} template tag
  #Easier to modify pathname here, and not hardcoded all over documents
  path('<int:question_id>/', views.detail, name='detail'),
  #/polls/4/results/
  path('<int:question_id>/results/', views.results, name='results'),
  #/polls/5/vote/
  path('<int:question_id>/vote/', views.vote, name='vote'),
]