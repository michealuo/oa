# Create your models here.

from django.db import models

#部门表
class Department(models.Model):

    name = models.CharField('部门名称',max_length=16)

# 员工表
class Management(models.Model):
    job_no = models.CharField('工号',max_length=16)
    management_job = models.CharField('部门职位',max_length=16)
    username = models.CharField('姓名',max_length=30)
    phone = models.CharField('手机号',max_length=32)
    create_time = models.DateTimeField('入职时间',auto_now_add=True)
    email = models.EmailField('邮箱',max_length=32,default=None)
    #是否入职（默认0 未入职，1 入职）
    department = models.ForeignKey(Department)
    def __str__(self):

        return '用户名:%s'%self.username