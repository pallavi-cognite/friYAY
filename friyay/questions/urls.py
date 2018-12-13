from django.urls import path
from . import views

urlpatterns = [
    path('allMeetings', views.all_meetings, name='all_meetings'),
    path('getMeeting', views.meeting, name='getMeeting'),
    path('createQuestion', views.create_question, name='create_question'),
    path('createResponse', views.create_response, name='create_response')
]
