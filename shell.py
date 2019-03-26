from django.utils import timezone

from polls.models import Choice, Question

Question.objects.all()

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

print(q.id)
print(q.question_text)
print(q.pub_date)

q.question_text = "What's up?"
q.save()

Question.objects.all()

Question.objects.filter(id=1)

Question.objects.filter(question_text__startswith='Wath')

current_year = timezone.now().year

Question.objects.get(pub_date__year=current_year)

Question.objects.get(id=2)

Question.objects.get(pk=1)

q = Question.objects.get(pk=1)
print(q.was_published_recently())

q = Question.objects.get(pk=1)
q.choice_set.all()
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

print(c.question)
q.choice_set.all()
q.choice_set.count()
Choice.objects.filter(question__pub_date__year=current_year)
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()