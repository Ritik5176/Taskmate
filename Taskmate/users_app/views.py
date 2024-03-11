from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomUserForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def Registration(request):
    if request.method=="POST":
        register_form=CustomUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("User is Created, Go to the Login"))
            return redirect('login')
    else:
        register_form= CustomUserForm()
    return render(request,'register.html',{'register_form': register_form})
