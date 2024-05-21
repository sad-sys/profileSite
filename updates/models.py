from django.db import models
from django import forms;

# Create your models here.
class Update(models.Model):
    Title =  models.CharField(max_length=50);
    date  = models.DateField
    content = models.TextField

