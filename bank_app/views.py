from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect("dashboard")  # Перенаправление после входа
    else:
        form = LoginForm()
    return render(request, "bank_app/login.html", {"form": form})


@login_required
def dashboard_view(request):
    return render(request, "bank_app/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Создаем пользователя
            login(request, user)  # Автоматически входим
            return redirect("dashboard")  # Перенаправляем в личный кабинет
    else:
        form = RegisterForm()
    return render(request, "bank_app/register.html", {"form": form})

