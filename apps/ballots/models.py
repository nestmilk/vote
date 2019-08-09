from datetime import datetime

from django.db import models

# Create your models here.
from logos.models import Logos
from voters.models import WXVoters


class Ballots(models.Model):
    voter = models.ForeignKey(WXVoters, verbose_name=u"微信选民")
    logo = models.ForeignKey(Logos, verbose_name=u"图标")
    add_time = models.DateTimeField(verbose_name=u"开始时间", default=datetime.now)

    class Meta:
        verbose_name = u"微信选票"
        verbose_name_plural = verbose_name

