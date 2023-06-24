from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag(name="total_count")
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('latest_post.html')
def show_latest(count=5):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post': latest_post}


@register.simple_tag
def most_commented_post(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))