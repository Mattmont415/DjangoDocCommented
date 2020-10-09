import datetime

from django.utils import timezone
from django.db import models


# Create your models here.
#database layout essentially
#Model is a source of TRUTH about yoru data, essential fields
#Migrations are derived from MODELS file

#each model is a class that subclasses models.Model
#Each model has class variables, represnting a database field in model

#when making changes to Models.py, MAKEMIGRATIONS POLLS
  #says we made some changes to our models, and stored as MIGRATION
#$ python manage.py sqlmigrate polls 0001
  #helps see what SQL Django thinks is required

class Question(models.Model):
  #Charfield REQUIRES maxlength
  # \/ field's name
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  #Add a __str__ to give a good representation for this model
  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
  #Defines a relationship, each CHOICE is related to a single QUESTION
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  #optional argument to 0 out the value
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text