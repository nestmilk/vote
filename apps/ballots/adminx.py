import xadmin
from ballots.models import Ballots


class BallotsAdmin(object):
    list_display = ['id', 'voter', 'logo', 'add_time']
    search_fields = ['id', 'voter', 'logo']
    list_filter = ['id', 'voter', 'logo', 'add_time']


xadmin.site.register(Ballots, BallotsAdmin)