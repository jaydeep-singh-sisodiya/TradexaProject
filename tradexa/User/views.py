from django.shortcuts import render,redirect
from .models import post
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    Posts = post.objects.all()
    params = {'posts':Posts}
    return render(request,'user/home.html',params)


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        username= request.POST['username']

        if(pass1!=pass2):
            messages.error(request,"Passwords do not match! Please try again.")
            return redirect('Home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Created!")
        return redirect('Home')



    else:
        return HttpResponse('404 - not found')

def login_func(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        password = request.POST['password']
        user = authenticate(username=loginusername, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are now Logged in as "+ user.username)
            return redirect('Home')
        else:
            messages.error(request,'Invalid Credentials, Please try again!')
            return redirect('Home')
    return HttpResponse('404-Not found')

def logout_func(request):
        logout(request)
        messages.success(request,"logged out")
        return redirect('Home')

def createpost(request):
    if request.method=="POST":
        user=request.user
        post1 = request.POST.get('createpost', "")
        post2 = post(text=post1, user=user)
        post2.save()
        messages.success(request,"Post Created Successfully!")
        return redirect("Home")
    else:
        return render(request,"User/createpost.html")
