from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginpg(request):
    return render(request,'user/login.html')

def signup(request):
    return render(request,'user/signup.html')


def loginmanage(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('loginpg')

def logoutmanage(request):
    logout(request)
    return redirect('home')


def signupmanage(request):
    if request.method=='POST':
        name=request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Error checks
        if len(username)>15:
            messages.error(request, 'Username must be less than 15 characters.')
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, 'Username must be alphanumeric.')
            return redirect('signup')
        
        if password!=cpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return redirect('signup')

        try:
            #Create User
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = name
            myuser.save()
            
            messages.success(request, 'Your Account Has Been Created Successfully.')
            return redirect('loginpg')
        except Exception as e:
            messages.error(request, 'An error occurred while creating your account. Please try again.')
            return redirect('signup')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('signup')

def account(request):
    return render(request,'user/account.html')
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# ...existing code...

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')
        
        # Verify password first
        if not user.check_password(password):
            return JsonResponse({'success': False, 'error': 'Incorrect password'})
        
        full_name = request.POST.get('full_name', '').split()
        email = request.POST.get('email')
        
        if len(full_name) >= 2:
            user.first_name = full_name[0]
            user.last_name = ' '.join(full_name[1:])
        elif len(full_name) == 1:
            user.first_name = full_name[0]
            user.last_name = ''
            
        user.email = email
        user.save()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)



