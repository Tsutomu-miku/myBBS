from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import BlogArticles

# Create your views here.

def index(request):
    return HttpResponse("hello world ")


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/titles.html',{"blogs":blogs})


def blog_article(request,article_id):
    # article = BlogArticles.objects.get(pk = article_id)
    article = get_object_or_404( BlogArticles,pk = article_id)
    # 可以用 try... except...捕获，在 except 中可以使用 raise Http404（）来处理
    pub = article.publish
    return render(request,'blog/content.html',{"article":article,"publish":pub })
