from django.db import models
from django.contrib.auth.models import User

# Class Category: Has name, user, will store tasks
class Category(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return f"{self.user}: {self.name}"

#Class Task: Has user, category, name, and active status
class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	active = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.category}: {self.name}"