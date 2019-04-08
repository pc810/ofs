from django.shortcuts import render, redirect
from .forms import UserForm, UserChangeForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import UpdateView

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

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/user_profile.html', {"user":user})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/users/")
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, "users/edit_profile.html", {"form":form})