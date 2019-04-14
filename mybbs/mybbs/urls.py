"""mybbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.generic import TemplateView#引用通用视图

from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    url('account/',include('account.urls')),
    path('article/',include('article.urls')),
    path('',TemplateView.as_view(template_name='home.html')),
    path('home/',TemplateView.as_view(template_name='home.html')),
    path('image/', include('image.urls', namespace='image')),
    path('course/', include('course.urls', namespace='course')),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATICFILES_DIRS[0]}, name='static'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}, name='static'),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
