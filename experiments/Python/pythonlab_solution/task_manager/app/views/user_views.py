from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_list(request):
    return render(request, 'users/user_list.html')


def user_create(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')
    else:
        user_form = UserCreationForm()

    return render(request, 'users/user_create.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, 'Login not valid')
            return redirect('user_login')
    else:
        login_form = AuthenticationForm()
    return render(request, 'users/login.html', {'login_form': login_form})


def user_logout(request):
    logout(request)
    return redirect('user_login')