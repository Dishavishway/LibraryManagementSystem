from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(null=False, max_length=30)
    enroll = models.IntegerField(default=0) 
    phone_number = models.CharField(max_length=20)
    email = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length= 20)  

class Book(models.Model):
    book_id = models.BigIntegerField(primary_key=True)
    book_name = models.CharField(max_length=100, null=False)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    price = models.IntegerField(default=100)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

