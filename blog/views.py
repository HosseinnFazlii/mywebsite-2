from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def blog_view(request,cat_name=None):
     today = timezone.now().date()
     posts=Post.objects.all()
     posts = Post.objects.filter(publish_date__lte=today, status=True)
     if cat_name:
      posts=posts.filter(category__name=cat_name)
     context={'post':posts}
     return render(request,'blog/blog-home.html',context )


def blog_single(request,pid):
       post=get_object_or_404(Post,pk=pid)
       post.counted_view +=1
       post.save()
       today = timezone.now().date()
       all_posts = Post.objects.filter(status=True, publish_date__lte=today).order_by('created_date')

    
       current_post_index = list(all_posts).index(post)

    
       previous_index = current_post_index - 1
       next_index = current_post_index + 1

    
       previous_post = all_posts[previous_index] if previous_index >= 0 else None
       next_post = all_posts[next_index] if next_index < len(all_posts) else None

       context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }


       return render(request,'blog/blog-single.html',context)



def blog_category(request,cat_name):
     today = timezone.now().date()
     posts=Post.objects.all()
     posts = Post.objects.filter(publish_date__lte=today, status=True)
     posts=posts.filter(category__name=cat_name)
     context={'post':posts}
     return render(request,'blog/blog-home.html',context )







