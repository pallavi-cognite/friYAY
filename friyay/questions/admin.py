from django.contrib import admin
from .models import Meeting
from .models import Question
from .models import Response


admin.site.register(Meeting)
admin.site.register(Question)
admin.site.register(Response)
