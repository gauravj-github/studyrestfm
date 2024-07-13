from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    
class Book(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    boot_title = models.CharField(max_length=100)
