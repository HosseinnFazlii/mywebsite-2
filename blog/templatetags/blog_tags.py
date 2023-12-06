from django import template
from blog.models import Post
from blog.models import Category

register= template.Library()

@register.filter
def snippet(value):
    return value[:100]


@register.inclusion_tag('blog/latestposts.html')
def latestposts():
    posts=Post.objects.filter(status=1).order_by('publish_date')[:3 ]
    return {'posts':posts}

@register.inclusion_tag('blog/post_categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    category=Category.objects.all()
    cat_dict={}
    for name in category:
        cat_dict[name]=posts.filter(category=name).count
    return {'categories':cat_dict} 