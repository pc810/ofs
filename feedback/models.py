from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.form_heading + " - " + self.user


class Question(models.Model):
    QUES_TYPE = (
        ('cho', 'choice'),
        ('chk', 'chk'),
        ('tx', 'text'),
        ('rg', 'range'),
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    ques_text = models.TextField()
    ques_type = models.CharField(choices=QUES_TYPE, max_length=10)

    def __str__(self):
        return self.form + " - "+ self.ques_text + " - " + self.ques_type


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    ans_posted = models.DateField(auto_now=True)

    def __str__(self):
        return self.user + " - " + self.form + " - " + self.question + " - " + self.answer
