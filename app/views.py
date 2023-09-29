from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    img = HomeSlider.objects.all()
    return render(request, 'home.html',{'img':img})
    


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html',{'blog':blog})

def details(request,slug):
    blog = Blog.objects.filter(blog_slug=slug)
    return render(request, 'details.html',{'blog':blog})



# Create your views here.
def signup(request):
    
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username: Username already exists')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email: Email already exists')
            return redirect('signup')
        if password==password2:
            myuser =User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
            myuser.save()
            messages.success(request, 'Account: Create successfully!')
           
        else:
            messages.error(request, 'Password: Password & Confirm Password do not match')    
            User.objects.filter(username=username).exists()
             
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "profile.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            
    
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

def profile(request):
    return render(request, 'profile.html')