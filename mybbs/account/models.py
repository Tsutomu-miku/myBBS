from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # 在数据库中简历名字为account_userprofile的字段 和User是一一对应的
    user = models.OneToOneField(User,unique = True,on_delete=models.CASCADE)

    birth = models.DateField(blank = True,null=True)
    phone = models.CharField(max_length=20,null = True)

    def __str__(self):
        return 'user {}'.format(self.username)

class UserInfo(models.Model):
    user = models.OneToOneField(User,unique = True,on_delete=models.CASCADE)
    school = models.CharField(max_length = 100,blank = True)
    company = models.CharField(max_length = 100,blank = True)
    profession = models.CharField(max_length = 100,blank = True)
    address = models.CharField(max_length = 100,blank = True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank =True)
    def __str__(self):
        return "user:{}".format(self.user.username)
 