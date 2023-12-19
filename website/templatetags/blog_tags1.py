from django import template
from blog.models import Post
from blog.models import Category

register= template.Library()

@register.filter
def snippet(value):
    return value[:100]


@register.inclusion_tag('website/latest_post.html')
def latest_posts():
    posts=Post.objects.filter(status=1).order_by('publish_date')[:6]
    return {'posts':posts}

