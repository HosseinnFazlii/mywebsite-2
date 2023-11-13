from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    email=models.EmailField()
    phone_number=models.IntegerField()
    content=models.CharField(max_length=300)
