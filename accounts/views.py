from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from posts.models import Post

# Create your views here.
def registration(request):
    if request.method == 'POST':
        #Create form instance
        form = RegisterForm(request.POST)
        if form.is_valid():
            #Get all data from form
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            check_username = User.objects.filter(username=username).exists()
            if check_username is True:
                return_data = {'form': form, 'error': 'A user with this username already exists.'}
            else:
                user = User.objects.create_user(username, email, password)
                auth_user = authenticate(username=username, password=password)
                if auth_user is not None:
                    login(request, user)
                    return redirect('account')
    else:
        form = RegisterForm()
        return_data = {'form': form }
    #Return to registration page
    return render(request, 'accounts/register.html', return_data)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/', user=user)
            else:
                return_data = {'form': form, 'error': 'Can\'t login account.'}
                return render(request, 'accounts/login.html', return_data)
    else:
        form = LoginForm()
        return_data = {'form': form}
        return render(request, 'accounts/login.html', return_data)

def account(request):
    if request.user.is_authenticated:
        posts_list = Post.objects.filter(author=request.user.id).order_by('-date_created')
        return_data = {'posts':posts_list}
        return render(request, 'accounts/account.html', return_data)
    else:
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')