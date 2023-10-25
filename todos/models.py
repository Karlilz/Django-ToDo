from django.db import models

# Create your models here.
#equivelent to models/schema in Mongoose 

class Todo(models.Model):
    subject = models.CharField(max_length=100) #subject is a string with max length of 100 
    details = models.CharField(max_length=100) #details is a string with a max length of 100 