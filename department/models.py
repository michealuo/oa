from django.db import models

# Create your models here.
#部门表
class Department(models.Model):

    name = models.CharField('部门名称',max_length=16)
    description = models.CharField('部门描述', max_length=64,default=None)

#职位表
class Position(models.Model):

    name = models.CharField('职位名称',max_length=16)
    dep_name = models.CharField('部门名称',max_length=16)
    description = models.CharField('职位描述',max_length=64)
    department = models.ForeignKey(Department)

