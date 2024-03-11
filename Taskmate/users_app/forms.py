from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    email=forms.EmailField()  #By Default is True means email mandatory, required=False for marking as a non mandatory
    class Meta:
        model= User
        fields=['username','email','password1','password2']