from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	#Displays URL patterns for index and welcome, both will be considered landing pages.
	path("", views.index, name="index"),
	path("welcome/", views.welcome, name="welcome"),

	#URL Paths on Categories.
	path("category/<int:category_id>", views.category, name="category"),
	path("add_category", views.add_category, name="add_category"),
	path("edit_category/<int:category_id>", views.edit_category, name="edit_category"),
	path("delete_category/<int:category_id>", views.delete_category, name="delete_category"),
	
	#URL Paths on Tasks.
	path("add_task/<int:category_id>", views.add_task, name="add_task"),
	path("delete_task/<int:task_id>", views.delete_task, name="delete_task"),
	path("mark_task/<int:task_id>", views.mark_task, name="mark_task"),
	path("delete_all_tasks <int:category_id>", views.delete_all_tasks, name="delete_all_tasks")
]