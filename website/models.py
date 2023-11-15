from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    email=models.EmailField()
    phone_number=models.IntegerField()
    content=models.CharField(max_length=300)
    created_date=models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ['created_date']
    def __str__(self):
        return self.name