
from django.urls import path , include
from blog.views import blog_view,blog_single

#app_name='website'

urlpatterns = [
    
    path('blog',blog_view,name='index'),
    path('blog/single',blog_single,name='single')
]
