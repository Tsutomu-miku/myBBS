from django import template
from django.db.models import Count

# 返回“安全”字符串
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from article.models import ArticlePost

# 注册一个实例对象register 这个对象包含了 simple_tag 方法是template.Library 的一个实例
@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag
def author_total_articles(user):
    return user.article.count()


# 返回数据应用于这个模板中
@register.inclusion_tag('article/list/latest_article.html')
def latest_articles(n = 5):
    latest_articles = ArticlePost.objects.order_by("-created")[:n]
    return {"latest_articles":latest_articles}

@register.simple_tag
def most_comment_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]

@register.filter(name='markdown')# 对下一句语句进行重命名
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))

