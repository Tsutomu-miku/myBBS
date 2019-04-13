
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # path('',views.index,name = 'index'),
    url(r'^$',views.blog_title,name="blog_title"),
    url(r'(?P<article_id>\d)/$',views.blog_article,name="blog_article"),
    # /$ 是最后 \d是数字  ?P 是组的表达方式
    # path('<int:article_id>/',views.blog_article,name="blog_article"),
]