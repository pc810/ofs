from django.db import models
from django.contrib.auth.models import User
import re
from django.urls import reverse


class Form(models.Model):
    FORM_STATUS = (
        ('AC', 'active'),
        ('DA', 'deactivated'),

    )
    form_heading = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_link = models.TextField()
    form_posted = models.DateField(auto_now=True)
    form_status = models.CharField(choices=FORM_STATUS, max_length=10)
    form_type = models.CharField(max_length=50, default="custom")

    class Meta:
        ordering = ["-form_posted"]

    def get_absolute_url(self):
        return reverse('feedback:feedback-index')

    def __str__(self):
        return self.form_heading

    class Meta:
        ordering = ["-form_posted"]


class Question(models.Model):
    QUES_TYPE = (
        ('cho', 'choice'),
        ('chk', 'chk'),
        ('tx', 'text'),
        ('rg', 'range'),
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    ques_text = models.CharField(max_length=500, default="notspecified")
    ques_type = models.CharField(choices=QUES_TYPE, max_length=10)
    ques_option = models.CharField(max_length=500, default="notspecified")
    quest_numb_option = models.IntegerField(default=1)

    def __str__(self):
        return self.ques_text + " - " + self.ques_type

    def question_as_list(self):
        regex = re.compile("([A-z_ -*+0-9]+).\(,\)")
        return regex.findall(self.ques_option)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    ans_posted = models.DateField(auto_now=True)

    def __str__(self):
        return self.answer


class response_user_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

