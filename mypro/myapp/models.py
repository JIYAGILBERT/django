from django.db import models

class Todoitem(models.Model):
    title= models.CharField(max_length=100)

# Create your models here.
