from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
import itertools
import datetime
from questions.models import Meeting, Question

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def all_meetings(request):
    meetings = Meeting.objects.all()
    data = serializers.serialize('json', meetings)
    return HttpResponse(data, content_type='application/json')

def meeting(request):
    meeting_id = request.GET.get('id', 0)
    meeting = Meeting.objects.get(pk=meeting_id)

    questions = meeting.question_set.all()

    question_list = []
    for question in questions:
        responses = question.response_set.all()
        response_list = []
        for response in responses:
            response_to_return = {
                'entry_text': response.entry_text,
                'creation_time': response.creation_time,
                'creator_name': response.creator_name,
                'upvotes': response.upvotes,
                'downvotes': response.downvotes
            }
            response_list.append(response)

        question_to_return = {
            'entry_text': question.entry_text,
            'creation_time': question.creation_time,
            'creator_name': question.creator_name,
            'upvotes': question.upvotes,
            'downvotes': question.downvotes,
            'responses': response_list
        }
        question_list.append(question_to_return)

    to_return = {
        'name': meeting.name,
        'questions': question_list
    }

    data = json.dumps(to_return, default = myconverter)
    # data = serializers.serialize('json', to_return)
    return HttpResponse(data, content_type='application/json')
