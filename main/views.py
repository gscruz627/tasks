from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from .models import Category, Task
from django.contrib import messages

''' Views.py from 'main' app
 - All pages are HTTP 404 protected.
 - Users 'own' their data, and the app will display only their data.
 - Some views will only receive, create, and redirect, and will not return any page.
'''

# Defines Index page, logged in users only. / Return Page
def index(request):

	if request.user.is_authenticated == False:
		return redirect("main:welcome")
	
	else:
		categories = Category.objects.filter(user=request.user)
		tasks = Task.objects.filter(user=request.user)
		context = {"categories":categories, "tasks":tasks}
		return render(request, "main/index.html", context)

# Defines 'Default' page, redirected from index if not logged in, main landing page / Return Page
def welcome(request):
	return render(request, "main/welcome.html")

# Defines individual category page, tasks will be displayed. / Return Page
@login_required
@csrf_protect
def category(request, category_id):
	
	category = Category.objects.get(id=category_id)
	
	if category.user != request.user:
		raise Http404
	
	categories = Category.objects.filter(user=request.user)
	tasks = Task.objects.filter(category_id=category_id)
	context = {"category":category, "tasks":tasks, "categories":categories}
	return render(request, "main/category.html", context)

# Defines loading page for adding a category / Return Redirect
@login_required
@csrf_protect
def add_category(request):
	
	user = request.user
	name = request.POST.get("categoryName")
	
	if not name:
		messages.add_message(request, messages.INFO, "Invalid Category Name")
		return redirect("main:index")

	Category.objects.create(user=user, name=name)
	return redirect("main:index")

# Defines loading page for editing a category / Return Redirect
@login_required
@csrf_protect
def edit_category(request, category_id):
	
	if request.method == "POST":
		category = Category.objects.get(id=category_id)
	
		if category.user != request.user:
			raise Http404
	
		new_name = request.POST.get("newName")
	
		if not new_name:
			messages.add_message(request, messages.INFO, "Invalid category name!, don't leave it blank!")
			return redirect("main:category", category_id=category_id)
	
		category.name = new_name
		category.save()
		messages.add_message(request, messages.INFO, "Category name changed successfully")
		return redirect("main:category", category_id=category_id)

# Defines loading page for deleting a category / Return Redirect
@login_required
def delete_category(request, category_id):
	
	category = Category.objects.get(id=category_id)
	
	if category.user != request.user:
		raise Http404
	
	category.delete()
	return redirect("main:index")

# Defines loading page for adding a task / Return Redirect
@login_required
@csrf_protect
def add_task(request, category_id):
	
	if request.method == "POST":
		user = request.user
		category = Category.objects.get(id=category_id)
	
		if category.user != request.user:
			raise Http404
	
		name = request.POST.get("new_task")
	
		if not name:
			messages.add_message(request, messages.INFO, "Invalid task name!, don't leave it blank!")
			return redirect("main:category", category_id=category_id)
	
		Task.objects.create(category=category, name=name, user=user)
		return redirect("main:category", category_id=category_id)

# Defines loading page for deleting a task / Return Redirect
@login_required
def delete_task(request, task_id):
	
	task = Task.objects.get(id=task_id)
	
	if task.user != request.user:
		raise Http404
	
	task.delete()
	return redirect("main:category", category_id=task.category.id)

# Defines loading page for marking a task as done or undone / Return Redirect
@login_required
def mark_task(request, task_id):
	
	task = Task.objects.get(id=task_id)
	
	if task.user != request.user:
		raise Http404
	
	if task.active:
		task.active = False
	
	else:
		task.active = True
	
	task.save()
	return redirect("main:category", category_id=task.category.id)

# Defines loading page for deleting all tasks marked done / Return Redirect
@login_required
def delete_all_tasks(request, category_id):
	
	category = Category.objects.get(id=category_id)
	
	if category.user != request.user:
		raise Http404
	
	tasks = Task.objects.filter(category=category).all()
	
	for task in tasks:
		if not task.active:
			task.delete()
	
	return redirect("main:category", category_id=category_id)

def error404(request, exception):
	return render(request, "main/error404.html")

def error500(request):
	return render(request, "main/error404.html")