from django.db import models

class Meeting(models.Model):
    name = models.CharField(max_length=150)
    creation_time = models.DateTimeField()
    password = models.CharField(max_length=100)
    archived = models.BooleanField()
    associated_questions = models.Choices()

# question, comment, or answer
class Entry(models.Model):

    entry_text = models.CharField()
    creation_time = models.DateTimeField()
    creator_name = models.CharField(max_length=150)
    upvotes = models.PositiveSmallIntegerField()
    downvotes = models.PositiveSmallIntegerField()

class Question(Entry):
    parent_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)

class Response(Entry):
    response_type_choices = (('question', 'Question'),
                             ('comment', 'Comment')
                             ('answer', 'Answer'))
    response_type = models.CharField(choices= response_type_choices, default='comment')
    parent_id = models.ForeignKey(Question, on_delete=models.CASCADE)
