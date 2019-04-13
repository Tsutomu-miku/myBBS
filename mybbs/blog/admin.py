from django.contrib import admin
from .models import BlogArticles
# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    # 显示这三列的内容
    list_filter = ("publish","author")
    # 右侧边过滤器
    search_fields = ('title','body')
    # 上方搜索区
    raw_id_fields = ('author',)
    # 显示外键的详细信息
    date_hierarchy = "publish"
    ordering = ['publish','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)
# admin.site.register(BlogArticles)