from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegistrationForm, LoginForm
from .models import Register, Login

def home(request):
	return render(request, "start/home.html")

def register(request):
	form = RegistrationForm()
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request, "start/register.html",{"form":form})

def login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,"start/login.html",{"forms":form})