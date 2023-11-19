from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def blog_view(request):
     posts=Post.objects.all()
     filtered_posts=[post for post in posts if post.status==1]

     return render(request,'blog/blog-home.html',{'post':filtered_posts} )

def blog_single(request,pid):
       post=get_object_or_404(Post,pk=pid)
       post.counted_view +=1
       post.save()
       context={'post':post,'pk':pid}

       return render(request,'blog/blog-single.html',context)



