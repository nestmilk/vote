from datetime import datetime

from django.db import models

# Create your models here.

class Logos(models.Model):
    pic = models.ImageField(verbose_name=u"商标图片",upload_to = "logos", max_length=100)
    desc = models.CharField(verbose_name=u'商标描述', max_length=300, default='', null=True, blank=True)
    vote_nums = models.IntegerField(verbose_name=u"投票数", default=0)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"商标"
        verbose_name_plural = verbose_name

