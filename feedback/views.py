from django.shortcuts import render
from .models import Form
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import NameForm
from django.contrib.auth.admin import User
from .models import Form as MyForm


def index(request):
    template_name = 'feedback/index.html'
    return render(request, template_name, None, None, None, None)


# class CreateFormClass(CreateView):
#     model = Form
#     fields = ['form_heading', 'form_status']
#     template_name = "feedback/form-template.html"
#     success_url = "feedback/add/question"

#def CreateForm(request):
    # template_name = 'feedback/form.html'
    #
    # if request.method == "POST":
    #     form_class = FormsForm(request.POST)
    #
    #     if form_class.is_valid():
    #         form = Form()
    #         form.user = request.user
    #         form.form_heading = form_class.cleaned_data["form_heading"]
    #         form.form_link = form_class.cleaned_data["form_link"]
    #         form.form_status = form_class.cleaned_data["form_status"]
    #         form.save()
    # else:
    #     form = FormsForm()
    #
    # return render(request, "feedback/form.html", {'form': form})


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
            return render(request, 'users/index.html')
        else:
            form = NameForm()

        return render(request, 'feedback/form.html', {'form': form})

