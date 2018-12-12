from django.db import models
from datetime import datetime

class Meeting(models.Model):
    name = models.CharField(max_length=150)
    creation_time = models.DateTimeField(default = datetime.now)
    password = models.CharField(max_length=100)
    archived = models.BooleanField()

# question, comment, or answer
class Entry(models.Model):

    entry_text = models.CharField(max_length=500, blank=True)
    creation_time = models.DateTimeField(default = datetime.now)
    creator_name = models.CharField(max_length=150, blank=True)
    upvotes = models.PositiveSmallIntegerField(default=0)
    downvotes = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True

class Question(Entry):
    parent = models.ForeignKey(Meeting, on_delete=models.CASCADE, default="")

class Response(Entry):
    response_type_choices = (('question', 'Question'),
                             ('comment', 'Comment'),
                             ('answer', 'Answer'))
    response_type = models.CharField(choices= response_type_choices, default='comment', max_length=100)
    parent = models.ForeignKey(Question, on_delete=models.CASCADE, default="")
