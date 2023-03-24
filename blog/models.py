
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    desc = models.TextField()
    photo = models.ImageField(upload_to='blogimages',blank=True)

class Contact(models.Model):
    name = models.TextField(max_length=70)
    email = models.EmailField(max_length=70)
    address = models.TextField(max_length=100)
    message = models.TextField(max_length=150)
