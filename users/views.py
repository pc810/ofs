from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

def index(request):
    template_name = 'users/index.html'
    return render(request, template_name, None, None, None, None)


def about(request):
    template_name = 'users/about.html'
    return render(request, template_name, None, None, None, None)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'users/registration_form.html', {'form': form})

