from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

 #   class Meta:
  #      model = User
   #     fields = ['username', 'email', 'password' ]


class UserForm(UserCreationForm):
    email = forms.EmailField()
    contact = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'contact']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']
