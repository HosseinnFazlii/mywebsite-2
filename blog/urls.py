
from django.urls import path , include
from blog.views import blog_view,blog_single

app_name='blog'

urlpatterns1 = [
    
    path('',blog_view,name='blog'),
    path('single/<int:pid>',blog_single,name='single'),
    
]
