from django.db import models

# Create your models here.
from user.models import User


class Report_list(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    user = models.ForeignKey(User)

    class Meta:
        db_table = "report_list"
