from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate
import re

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if 'username' in request.session:
        return redirect('home')
  
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']  

    
        if(not first_name ):
            messages.info(request, 'Firstname required ') 
            return redirect('register')
        elif re.match("/^[a-z ,.'-]+$/i", first_name) != None:
            messages.info(request, 'Firstname required characters ') 
            return redirect('register')
        elif(not last_name):
            messages.info(request, 'Lastname required')
            return redirect('register')
        if len(email) > 12:
            if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email) != None:
                messages.info(request, 'Valid email required')
                return redirect('register')
        elif len(email) < 12:
            messages.info(request, 'Need atleast 6 in mail')
            return redirect('register')

        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist') 
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, first_name = first_name, last_name = last_name, password = password1)
                user.save();
                #request.session['username'] = username
                print('user created')
                return redirect('login')
            
        else:
            messages.info(request,"password not matching")
            return redirect('register')
     
    else:
        return render(request, 'register.html')   
    
    """
    if request.method == "POST":
        print(request.POST)
    
        registerForm = registerForm(request.POST)
        office = registerForm.save()

     
        return JsonResponse({"message" :"Request handle"})
        

    else:
        return render(request, 'register.html')
    """ 

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'username' in request.session:
         return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            auth.login(request,user)
            return redirect('/')
           
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
            
            
    else:
        return render(request, 'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    
        request.session.flush()
        return redirect('home')
   