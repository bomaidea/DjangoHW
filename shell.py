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

