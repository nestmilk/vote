import xadmin
from voters.models import WXVoters


class WXVotersAdmin(object):
    list_display = ['id', 'openid', 'headimgurl', 'add_time']
    search_fields = ['id', 'openid', 'headimgurl']
    list_filter = ['id', 'openid', 'headimgurl', 'add_time']


xadmin.site.register(WXVoters, WXVotersAdmin)