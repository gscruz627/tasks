from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
	#INCLUDES DJANGO'S OWN URLS FOR LOGIN, LOGOUT.
	path("", include("django.contrib.auth.urls")),
	path("register/", views.register, name="register"),
	path("change_name/", views.change_name, name="change_name"),
]