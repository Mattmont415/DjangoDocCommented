
from django.urls import path
#From current directory, import the VIEWS file

from . import views

urlpatterns = [
  #/polls/
  path('', views.index, name='index'),

  #/polls/5
  path('<int:question_id>/', views.detail, name='detail'),
  #/polls/4/results/
  path('<int:question_id>/results/', views.results, name='results'),
  #/polls/5/vote/
  path('<int:question_id>/vote/', views.vote, name='vote'),
]