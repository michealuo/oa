from django.db import models
from user.models import User
# Create your models here.
class TimeBook(models.Model):
    date = models.DateField('日期')
    is_commen = models.BooleanField('是否正常',default=True)
    is_absent = models.BooleanField('是否旷工',default=False)
    is_leave = models.BooleanField('是否请假',default=False)
    is_late = models.BooleanField('是否迟到',default=False)
    is_leave_early = models.BooleanField('是否早退',default=False)
    comment = models.CharField('备注',max_length=100,default='')
    user = models.ForeignKey(User)


    class Meta:
        db_table = 'timebook'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = None

    def __str__(self):
        return '%s_%s_%s'%(self.user_id,self.date,self.is_commen)