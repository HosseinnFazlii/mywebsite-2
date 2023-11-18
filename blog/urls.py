
from django.urls import path , include
from blog.views import blog_view,blog_single,test

app_name='blog'

urlpatterns1 = [
    
    path('',blog_view,name='index'),
    path('single',blog_single,name='single'),
    path('<int:pid>',test,name='test')
]
