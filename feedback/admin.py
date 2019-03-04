from django.contrib import admin
from .models import Question, Answer, Form


admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Answer)

