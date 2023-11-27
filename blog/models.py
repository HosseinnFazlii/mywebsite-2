from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content = models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    publish_date=models.DateTimeField(null=True)
    status=models.BooleanField(default=False)
    counted_view=models.IntegerField(default=0)
    image=models.ImageField(upload_to='media/',default='media/blog/default.jpg')
    

    def __str__(self):
        return "{}-{}-{}".format(self.title,self.status,self.id)