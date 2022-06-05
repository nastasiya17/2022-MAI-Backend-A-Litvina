from django.db import models

from category.models import Category

class Showplace(models.Model):
    name=models.CharField(max_length=128)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)

