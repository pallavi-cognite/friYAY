from django.urls import path
from . import views

urlpatterns = [
    path('allMeetings', views.all_meetings, name='all_meetings'),
    path('meeting', views.meeting, name='meeting')
]
