from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField('账号',max_length=30)
    password = models.CharField('密码',max_length=32)
    phone = models.CharField('手机号',max_length=32)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    email = models.EmailField('邮箱',max_length=32,default=None)


    def __str__(self):

        return '用户名:%s'%self.username