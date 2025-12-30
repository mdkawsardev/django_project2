from django.db import models

# Create your models here.
class Contact(models.Model): #? I created a model named Contact
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    desc = models.TextField()
    date = models.DateField()