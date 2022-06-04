from django.db import models

from category.models import Category

class Showplace(models.Model):
    name=models.CharField(max_length=128)
    category=models.CharField(max_length=128)
    
'''    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        ordering = ("name", "category")
    
    def __str__(self):
        return self.name + ", " + self.category
'''