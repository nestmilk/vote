from datetime import datetime

from django.db import models

# Create your models here.

class WXVoters(models.Model):
    openid = models.CharField(verbose_name=u"微信openid", max_length=100, unique=True)
    headimgurl = models.URLField(verbose_name=u"头像url", max_length=500)
    add_time = models.DateTimeField(verbose_name=u"开始时间", default=datetime.now)

    class Meta:
        verbose_name = "微信选民"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.openid
