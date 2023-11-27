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
       all_posts = Post.objects.order_by('created_date')

    # Find the index of the current post
       current_post_index = list(all_posts).index(post)

    # Calculate indices for previous and next posts
       previous_index = current_post_index - 1
       next_index = current_post_index + 1

    # Check if there are previous and next posts
       previous_post = all_posts[previous_index] if previous_index >= 0 else None
       next_post = all_posts[next_index] if next_index < len(all_posts) else None

       context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }


       return render(request,'blog/blog-single.html',context)



