from django.shortcuts import redirect, render
from django.contrib import messages
from authapp.models import Custmers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    if request.user.is_anonymous:
        return redirect('authlogin')
    return render(request,'home.html')

def authregister(request):
    if request.method =='POST':
        authusername = request.POST['authusername']
        authemail = request.POST['authemail']
        authpassword = request.POST['authpassword'] 
        myuser = User.objects.create_user(authusername,authemail,authpassword)
        myuser.save()
        messages.success(request,"successfull!")
        return redirect('authlogin')
    else:
        messages.error(request,"error 404")
    
    return render(request,'register.html')
      

def authlogin(request):
    if request.method =='POST':
        authusername = request.POST['authusername']
        authpassword = request.POST['authpassword'] 
        
        user = authenticate(username=authusername,password=authpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"done")
            return redirect('/')
        else: 
            messages.error(request,"not found")            

    return render(request,'login.html')


def authlogout(request):
    logout(request)

    return redirect('authlogin')
