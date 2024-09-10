from django.shortcuts import render,redirect
from .forms import SignupForm, LoginForm, ChangepasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .models import CustomerUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    data = CustomerUser.objects.all()
    context={
        'data': data,
    }
    return render(request, 'app/home.html',context)

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been registered Successfully!!!')
            return redirect('login')
    else:
         fm = SignupForm()      
    context={
        'fm': fm,
    }
    return render(request, 'app/signup.html',context)

def user_login(request):
    if request.method =='POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(email=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        fm = LoginForm()
    context={
        'fm': fm,
    }
    return render(request, 'app/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def user_change_pass(request):
    if request.method == 'POST':
        fm = ChangepasswordForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'Password has been Changed Successfully!!!')
            return redirect('home')
    else:
        fm = ChangepasswordForm(user=request.user)
    context={
        'fm': fm,
    }
    return render(request, 'app/change_password.html', context)