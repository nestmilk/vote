from logos.models import Logos
from extra_apps import xadmin


class LogosAdmin(object):
    list_display = ['id','pic','desc','vote_nums','add_time']
    search_fields = ['desc']
    list_filter = ['id','pic','desc','vote_nums','add_time']


xadmin.site.register(Logos, LogosAdmin)