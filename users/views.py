from django.shortcuts import render
from django.views import generic


def index(request):
    template_name = 'users/index.html'
    return render(request, template_name, None, None, None, None)
