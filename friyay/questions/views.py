from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from rest_framework import serializers as rest_serializer
from rest_framework.parsers import JSONParser
import json
import itertools
import datetime
from questions.models import Meeting, Question, Response
from django.views.decorators.csrf import csrf_exempt

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

class QuestionSerializer(rest_serializer.ModelSerializer):
    parent = rest_serializer.PrimaryKeyRelatedField(queryset=Meeting.objects.all())
    class Meta:
       model = Question
       fields = ('entry_text', 'creator_name', 'parent')

@csrf_exempt
def create_question(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = QuestionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)

        return HttpResponse(serializer.errors, status=400)

class ResponseSerializer(rest_serializer.ModelSerializer):
    parent = rest_serializer.PrimaryKeyRelatedField(queryset=Question.objects.all())
    class Meta:
       model = Response
       fields = ('entry_text', 'creator_name', 'parent', 'response_type')

@csrf_exempt
def create_response(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = ResponseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)

        return HttpResponse(serializer.errors, status=400)


# SORT BY TIME!
# THEN FIGURE OUT HOW TO MAKE POST REQUESTS
def all_meetings(request):
    meetings = Meeting.objects.all()
    meeting_list = []
    for meeting in meetings:
        meeting_to_return = {
            'name': meeting.name,
            'creation_time': meeting.creation_time,
            'archived': meeting.archived,
            'id': meeting.pk,
        }
        meeting_list.append(meeting_to_return)


    # data = serializers.serialize('json', meetings)
    meeting_list.sort(key=lambda x: x['creation_time'], reverse=True)
    data = json.dumps(meeting_list, default = myconverter)
    return HttpResponse(data, content_type='application/json')

def meeting(request):
    meeting_id = request.GET.get('id', 0)
    meeting = Meeting.objects.get(pk=meeting_id)

    questions = meeting.question_set.all()

    question_list = []
    for question in questions:
        responses = question.response_set.all().order_by('creation_time')
        response_list = []
        for response in responses:
            response_to_return = {
                'id': response.pk,
                'text': response.entry_text,
                'creation_time': response.creation_time,
                'creator_name': response.creator_name,
                'upvotes': response.upvotes,
                'downvotes': response.downvotes
            }
            response_list.append(response_to_return)

        question_to_return = {
            'id': question.pk,
            'text': question.entry_text,
            'creation_time': question.creation_time,
            'creator_name': question.creator_name,
            'upvotes': question.upvotes,
            'downvotes': question.downvotes,
            'responses': response_list
        }
        question_list.append(question_to_return)

    question_list.sort(key=lambda x: (x['upvotes'] - x['downvotes']), reverse=True)
    to_return = {
        'name': meeting.name,
        'archived': meeting.archived,
        'questions': question_list
    }

    data = json.dumps(to_return, default = myconverter)
    # data = serializers.serialize('json', to_return)
    return HttpResponse(data, content_type='application/json')
