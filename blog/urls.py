
from django.urls import path , include
from blog.views import blog_view,blog_single

#app_name='website'

urlpatterns1 = [
    
    path('',blog_view,name='index'),
    path('single',blog_single,name='single')
]
