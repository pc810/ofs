from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from .forms import UserForm
from django.views.generic import View

def index(request):
    template_name = 'users/index.html'
    return render(request, template_name, None, None, None, None)
def about(request):
    template_name = 'users/about.html'
    return render(request, template_name, None, None, None, None)

class UserFormView(View):
    form_class = UserForm
    template_name = 'users/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    return redirect('users:index')

        return render(request, self.template_name, {'form': form})

