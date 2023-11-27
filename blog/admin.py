from django.contrib import admin
from blog.models import Post,Category
# Register your models here.ad



class AuthorAdmin(admin.ModelAdmin):
 list_display = [ "title","status","id","author"]
 
admin.site.register(Category)
admin.site.register(Post,AuthorAdmin)
