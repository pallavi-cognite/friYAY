from tastypie.resources import ModelResource
from questions.models import Meeting, Question, Response
from tastypie.authorization import Authorization

# all meetings, meetings with questions
class MeetingResource(ModelResource):
    class Meta:
        queryset = Meeting.objects.all()
        resource_name = 'meeting'
        authorization = Authorization()

class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
        authorization = Authorization()

class ResponseResource(ModelResource):
    class Meta:
        queryset = Response.objects.all()
        resource_name = 'response'
        authorization = Authorization()
