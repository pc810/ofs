from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    template_name = 'feedback/index.html'
    return render(request, template_name, None, None, None, None)

