from django.contrib import admin
from .models import Question, Answer, Form, response_user_list


admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(response_user_list)

