from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length = 300)
    author = models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)
    # django 2.0后，on_delete 是必填项
    # on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
    # on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
    # on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
    # on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
    # # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    # on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
    # # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    # on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
    # on_delete=models.SET,         # 删除关联数据,

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
    # 规定了BlogArticles 实例对象的显示顺序
        ordering = ("-publish",)
        # 按照出版日期降序显示
        # 直接写是升序
        # ordering = ("?publish",) 表示随机排序
    
    def __str__(self):
        return self.title


