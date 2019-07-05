from django.db import models

# Create your models here.
from django.utils.timezone import now

class Test2(models.Model):
    name = models.CharField("姓名", max_length=200)
    age = models.IntegerField("年龄", default=1)

class User(models.Model):
    name = models.CharField("姓名", max_length=250, null = False, default="")
    age = models.IntegerField("年龄", max_length= 4, null= False, default= 1)
    desc = models.CharField("座右铭", max_length=250, null = False, default="")
    update_date = models.DateField("更新时间", default=now)