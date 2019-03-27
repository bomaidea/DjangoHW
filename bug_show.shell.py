import datetime

from django.utils import timezone

from polls.models import Question


future_questiom = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
print(future_question.was_published_recently())
