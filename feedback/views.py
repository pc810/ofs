from django.shortcuts import render, redirect
from .models import Form
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .forms import NameForm
from django.contrib.auth.admin import User
from .models import Form as MyForm
from .models import Question as MyQuestion
from .models import Answer as MyAnswer

import re

def index(request):
    template_name = 'feedback/index.html'
    if request.user.id:
        userform = MyForm.objects.filter(user=request.user)
        return render(request, template_name, {'userform': userform})
    else:
        return render(request, template_name)


def createForm(request):
        if request.method == 'POST':
            form = NameForm(request.POST)
            if form.is_valid():
                user = User.objects.filter(pk=request.user.id)[0]
                myform = MyForm()
                myform.user = user
                myform.form_heading = form.cleaned_data["form_heading"]
                myform.form_link = form.cleaned_data["form_link"]
                myform.form_status = form.cleaned_data["form_status"]
                myform.save()

            return render(request, 'users/index.html', {'myform': myform})

        else:
            form = NameForm()

        return render(request, 'feedback/form.html', {'form': form})


def displayForm(request):
    if request.user.is_authenticated:
        q = MyQuestion()
        userform = MyForm.objects.filter(user=request.user)
        return render(request, "feedback/userform.html", {"userforms": userform})


def manage(request):
    if request.POST.get("myaction", "") == "addquestion":
        return addQuestion(request)


    if request.GET.get("myaction", "") == "edit":
        return editForm(request)
    elif request.GET.get("myaction", "")=="share":
        return shareForm(request)
    elif request.GET.get("myaction", "")=="response":
        return viewResponse(request)
    elif request.GET.get("myaction", "")=="addquestion":
        return addQuestion(request)
    elif request.GET.get("myaction", "")=="remove":
        return removeForm(request)
    else:
        return render(request, "feedback/myaction.html", {'myaction': request.GET.get("myaction", "") , 'id': request.GET.get("formid", "")})


def addQuestion(request):
    if request.method == "POST":

        ques_text = ""
        quest_numb_option = 0
        if request.POST.get("type", "") == 'cho':
            option1 = request.POST.get("option1", "")
            option2 = request.POST.get("option2", "")
            option3 = request.POST.get("option3", "")
            option4 = request.POST.get("option4", "")

            if option1 != "":
                ques_text+=option1+" (,)"
                quest_numb_option+=1
            if option2 != "":
                ques_text+=option2+" (,)"
                quest_numb_option += 1
            if option3 != "":
                ques_text+=option3+" (,)"
                quest_numb_option += 1
            if option4 != "":
                ques_text+=option4+" (,)"
                quest_numb_option += 1
        elif request.POST.get("type", "") == 'chk':
            option1 = request.POST.get("option1", "")
            option2 = request.POST.get("option2", "")
            option3 = request.POST.get("option3", "")
            option4 = request.POST.get("option4", "")

            if option1 != "":
                ques_text+=option1+" (,)"
                quest_numb_option += 1
            if option2 != "":
                ques_text+=option2+" (,)"
                quest_numb_option += 1
            if option3 != "":
                ques_text+=option3+" (,)"
                quest_numb_option += 1
            if option4 != "":
                ques_text+=option4+" (,)"
                quest_numb_option += 1

        elif request.POST.get("type", "") == 'tx':
            mytextarea = request.POST.get("mytextarea", "")
            ques_text = mytextarea
            quest_numb_option += 1
        elif request.POST.get("type", "") == 'rg':
            myrange = request.POST.get("myrange", "")
            ques_text = myrange
            quest_numb_option += 1
        # return render(request,
        #               "feedback/myaction.html",
        #               {
        #                   "id": request.POST.get("formid", ""),
        #                   "question_description": request.POST.get("question_description", ""),
        #                    "type": request.POST.get("type", ""),
        #                   # "option1": request.POST.get("option1", ""),
        #                   # "option2": request.POST.get("option2", ""),
        #                   # "option3": request.POST.get("option3", ""),
        #                   # "option4": request.POST.get("option4", ""),
        #                   # "mytextarea": request.POST.get("mytextarea", ""),
        #                   # "myrange": request.POST.get("myrange", ""),
        #                   "ques_text": ques_text,
        #               }
        #               )
        id = request.POST.get("formid", "")
        userform = MyForm.objects.filter(pk=id)[0]
        userquestion = MyQuestion()
        userquestion.form = userform
        userquestion.quest_numb_option = quest_numb_option
        userquestion.ques_text = request.POST.get("question_description", "")
        userquestion.ques_type = request.POST.get("type", "")
        userquestion.ques_option = ques_text

        userquestion.save()
        return render(request, 'users/index.html')

    else:
        if request.GET.get("type", "") == "":
            type = "chk"
        else:
            type = request.GET.get("type", "")

        if request.GET.get("formid", "") == "":
            return render(request, 'feedback/index.html')
        else:
            formid = request.GET.get("formid", "")

        return render(request,
                      "feedback/question.html",
                      {'myaction': "add question",
                       'id': request.GET.get("formid", ""),
                       'type': type,
                        'formid': formid,
                       },
                      )


def editForm(request):
    return redirect('form/update/'+request.GET.get("formid", ""))


def shareForm(request):
    return render(request, "feedback/myaction.html",{'myaction': "share", 'id': request.GET.get("formid", "")})


def viewResponse(request):
    return render(request, "feedback/myaction.html",{'myaction': "viewResponse", 'id': request.GET.get("formid", "")})


def removeForm(request):
    userform = MyForm.objects.filter(pk=request.GET.get("formid", ""))[0].delete()
    return redirect('/feedback')


def aboutForm(request, formid):
    userform = MyForm.objects.filter(pk=formid)[0]
    questions = MyQuestion.objects.filter(form=userform)
    return render(request,
                  "feedback/form-about.html",
                  {"form": userform,
                   "questions": questions,
                   },
                  )


class UpdateForm(UpdateView):
    model = MyForm
    fields = ["form_heading", "form_status", "form_type"]

def formResponse(request, formid):
    userform = MyForm.objects.filter(pk=formid)[0]
    questions = MyQuestion.objects.filter(form_id=formid)
    return render(request,
                  "response/form-answer.html",
                  {
                      "form": userform,
                      "questions": questions,
                  },
                  )


def subans(request):

    formid = request.POST.get("formid", "")
    questions = MyQuestion.objects.filter(form_id=formid)
    for q in questions:
        userans = MyAnswer()
        userans.form = MyForm.objects.filter(pk=formid)[0]
        userans.user = request.user
        userans.question = q;
        answer = ""
        regex = re.compile("([A-z_ -*+0-9]+).\(,\)")
        optionlist = regex.findall(q.ques_option)
        if q.ques_type == 'chk':
            for option in optionlist:
                param = str(q.id) +"-"+ str(option)
                if request.POST.get(param, "") == option:
                    answer += str(option) + " (,)"
        else:
            param = str(q.id)
            answer = request.POST.get(param, "")

        userans.answer = answer

        userans.save()

    return redirect("/feedback/")
