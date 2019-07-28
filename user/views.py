from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def register(request):
    form =RegisterForm(request.POST or None)
    if form.is_valid():
        username =form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser =User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.info(request,"your registration was complete")
        return redirect("index")
    context ={
        "form":form
    }    
    return render(request,"register.html",context)     
        
    

def signin(request):
    form =LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password =form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"username or password is invalid")
            return render(request,"login.html",context)
        messages.success(request,"you logined")
        login(request,user)
        return redirect("index")

    messages.info(request,"username or password is invalid")
    return render(request,"login.html",context)



def signout(request):
    logout(request)
    messages.success(request,"you signed out")
    return redirect("index")
