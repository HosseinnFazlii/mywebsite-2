from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    publish_date=models.DateTimeField(null=True)
    status=models.BooleanField(default=False)
    counted_view=models.IntegerField(default=0)
    

    def __str__(self):
        return "{}-{}-{}".format(self.title,self.status,self.id)