
from django.urls import path , include
from blog.views import index_view,about_view

#app_name='website'

urlpatterns = [
    
    path('blog',blog_view,name='index'),
    path('blog/single',blog_single,name='single')
]
