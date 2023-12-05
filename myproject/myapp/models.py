from django.db import models

# Create your models here.
class Teacher(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email_id = models.EmailField(max_length=20)
    Contact = models.CharField(max_length=20)


def __init__(self) ->str:   #this function is used to convert objects into string
    return self.First_name
