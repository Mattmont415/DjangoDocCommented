import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


#This becomes the question shortcut function
def create_question(question_text, days):
  """
  Create a question with the given 'question_text' and published the given number of 'days'
  offset to now (nega for q's pubbed in past, positive for not yet pubbed).
  """
  time = timezone.now() + datetime.timedelta(days=days)
  return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
  #Checks to see if empty no polls are avaialble, verifies latestqlist is empty
  def test_no_questions(self):
    """
    If no questions exist, an approrpiate message should be displayed
    """
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])
  
  def test_past_question(self):
    """
    Questions with pubdate in past are displayed on index page
    """
    create_question(question_text="Past quest.", days=-30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      ['<Question: Past quest.>']
    )

  def test_future_question(self):
    """
    Questions with a future pub date shouldnt be displayed
    """
    create_question(question_text="Future quest", days=30)
    response = self.client.get(reverse('polls:index'))
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_future_question_and_past_question(self):
    """
    Even if both past and future quetsions exist, only past quests are displayed
    """
    create_question(question_text="Past quest", days=-30)
    create_question(question_text="Future quest", days=30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      ['<Question: Past quest>']
    )

  def test_two_past_questions(self):
    """
    The questions index page may display multiple questions
    """
    create_question(question_text="Past question 1.",days=-30)
    create_question(question_text="Past question 2.", days=-5)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      ['<Question: Past question 2.>', '<Question: Past question 1.>']
    )


#Testing to make sure that the user cannot type in a poll in the future and figure it out
class QuestionDetailViewTests(TestCase):
  def test_future_question(self):
    """
    The detail view of a question with a pub_date in the future returns 404 not found
    """
    future_question = create_question(question_text='Future question', days=5)
    url = reverse('polls:detail', args=(future_question.id,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

  def test_past_question(self):
    """
    The detail view of a question with a pub_date in the past displays the q's text
    """
    past_question = create_question(question_text="Past quest.", days=-5)
    url = reverse('polls:detail', args=(past_question.id,))
    response = self.client.get(url)
    self.assertContains(response, past_question.question_text)

# The testcase subclass with a method that creates a Question instance with pubdate
# in the future. Check output which OUGHT to be false
class QuestionModelTests(TestCase):
  def test_was_published_recently_with_future_question(self):
    """
    was_published_recently() returns False for questions whose pub_date is in future
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    self.assertIs(future_question.was_published_recently(), False)

  def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)

#When we ran the test, what happened?
# Manage.py test polls looked for tests in polls app, and FOUND it
# Created a DB for testing, looked for test methods (begin with test)
# Created question instance in long method, with 30 days in future. 
# Using assertIs (assert that it is) returns true so we're told "True is not False"
# Now go to models.py and amend it so that it will be true IFOF in the past
