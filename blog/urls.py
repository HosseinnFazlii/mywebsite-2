
from django.urls import path , include
from blog.views import blog_view,blog_single,blog_category

app_name='blog'

urlpatterns1 = [
    
    path('',blog_view,name='blog'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_category,name='category'),
]
 