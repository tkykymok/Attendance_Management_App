from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Date(models.Model):
    masterdate = models.DateField(verbose_name='日付',default=datetime.today, unique=True)
    def __str__(self):
        return str(self.masterdate)
    
class CheckInOut(models.Model):
    staff = models.ForeignKey(User, verbose_name='社員', on_delete=models.PROTECT, null=True, blank=True)
    date_worked = models.ForeignKey(Date, verbose_name='日付', on_delete=models.PROTECT, default=datetime.today)
    check_in = models.TimeField(verbose_name='出勤時刻',null=True, blank=True)
    check_out = models.TimeField(verbose_name='退勤時刻',null=True, blank=True)
    overtime_s =  models.TimeField(verbose_name='残業開始', null=True, blank=True)
    overtime_e =  models.TimeField(verbose_name='残業終了', null=True, blank=True)
    remark =  models.CharField(verbose_name='備　　考', max_length=30, null=True, blank=True)
    total_overtime = models.IntegerField(verbose_name='残業時間合計(分)', null=True, blank=True)
    
    def __str__(self):
        return str(self.date_worked) 
    
