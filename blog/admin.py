from django.contrib import admin
from blog.models import Post
# Register your models here.ad



class AuthorAdmin(admin.ModelAdmin):
 list_display = [ "title","status","id"]
 
admin.site.register(Post,AuthorAdmin)