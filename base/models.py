from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.date.today)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class HistoryModel(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    deleted_at = models.DateField(default=datetime.date.today)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class CompletedModel(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    completed_at = models.DateField(default=datetime.date.today)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=1000)
    host=models.ForeignKey(User,on_delete=models.CASCADE)




