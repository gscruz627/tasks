from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Defines view for the registration page, POST, GET / Return Page (GET), Redirect (POST).
def register(request):
	
	if request.method == "POST":
		form = UserCreationForm(data=request.POST)
	
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect("main:index")
	
	else:
		form = UserCreationForm()
	
		if request.user.is_authenticated:
			messages.add_message(request, messages.INFO, "You are already logged in!, log out and try signing up again!")
			return redirect("main:index")
	
	context = {form:"form"}
	return render(request, "registration/register.html", context)

@login_required
def change_name(request):

	new_name = request.POST.get("newName")

	if not new_name:
		return redirect("main:index")

	request.user.username = new_name
	request.user.save()
	return redirect("main:index")	