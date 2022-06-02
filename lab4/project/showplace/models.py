from django.db import models

from category.models import Category

class Showplace(models.Model):
    sh_name=models.CharField(max_length=128)
    sh_category=models.ForeignKey(Category, on_delete=models.CASCADE)
