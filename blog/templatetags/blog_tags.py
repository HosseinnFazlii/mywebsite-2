from django import template
from blog.models import Post

register= template.Library()

@register.filter
def snippet(value):
    return value[:100]


@register.inclusion_tag('blog/latestposts.html')
def latestposts():
    posts=Post.objects.filter(status=1).order_by('publish_date')[:3 ]
    return {'posts':posts}