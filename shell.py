from django.utils import timezone

from polls.models import Choice, Question

# empty table
Question.objects.all()
# <QuerySet []>

# create new question with text and pub_date
q = Question(question_text="What's new?", pub_date=timezone.now())
# save question in db
q.save()

# print id
print(q.id)
# 1

# print text of the question
print(q.question_text)
# What's new?

# print the pub_date of the question
print(q.pub_date)
# 2019-03-26 20:40:46.355213+00:00

# change the text of the question
q.question_text = "What's up?"

# update question in db
q.save()

# display all questions in db
Question.objects.all()
# <QuerySet [<Question: Question object(1)>]>

# add the methods to the polls/models (add the __str__() methods)

# display all question in db
Question.objects.all()
# <QuerySet [<Question: What's up?>]>

# get Question element with id 1
Question.objects.filter(id=1)
# <QuerySet [<Question: What's up?>]>

# get Question elements with text starting with 'Wath'
Question.objects.filter(question_text__startswith='Wath')
# <QuerySet [<Question: What's up?>]>

# set the current year
current_year = timezone.now().year

# get Question elements with pub_date in current year
Question.objects.get(pub_date__year=current_year)
# <QuerySet [<Question: What's up?>]>

# get Question element with id 2
Question.objects.get(id=2)
# Error

# get Question with primary key 1
Question.objects.get(pk=1)
# <QuerySet [<Question: What's up?>]>

# q to Question with pk=1
q = Question.objects.get(pk=1)
# <QuerySet [<Question: What's up?>]>

# print q.was_published_recently()
print(q.was_published_recently())
# True

# display all choices of q
q.choice_set.all()
# <QuerySet []>

# Create three choices.
q.choice_set.create(choice_text='Not much', votes=0)
# <Choice: Not much>
q.choice_set.create(choice_text='The sky', votes=0)
# <Choice: The sky>

# Set new choice to c
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# print the question of c
print(c.question)
# <Question What's up?>

# print all choice of q
q.choice_set.all()
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# counting the choice of q
q.choice_set.count()
# 3

# show  choice of questions published in this year
Choice.objects.filter(question__pub_date__year=current_year)
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# set to c the choice of q starting with 'Just hacking'
c = q.choice_set.filter(choice_text__startswith='Just hacking')
# deleting c
c.delete()