import json

import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View

from ballots.models import Ballots
from logos.models import Logos
from vote.settings import APPID, APPSECREAT
from voters.models import WXVoters


class AuthorizeView(View):
    """
    微信授权
    """
    def get(self, request):
        url_params ={
            'appid': APPID,
            'redirect_uri': 'http://pombase.natapp1.cc/userInfo',
            'response_type': 'code',
            'scope': 'snsapi_userinfo',
            'state': '123'
        }

        return HttpResponseRedirect('https://open.weixin.qq.com/connect/oauth2/authorize?'+
                                    'appid=' + url_params['appid'] +
                                    '&redirect_uri=' + url_params['redirect_uri'] +
                                    '&response_type=' + url_params['response_type'] +
                                    '&scope=' + url_params['scope'] +
                                    '&state=' + url_params['state'] +
                                    '&connect_redirect=1'
                                    )


class UserInfoView(View):
    """
    获取微信个人信息
    """
    def get(self, request):
        code = request.GET.get('code')
        url_params ={
            'appid': APPID,
            'secret': APPSECREAT,
            'code': code,
            'grant_type': 'authorization_code'
        }
        access_token_response = requests.get('https://api.weixin.qq.com/sns/oauth2/access_token?'+
                                'appid=' + url_params['appid'] +
                                '&secret=' + url_params['secret'] +
                                '&code=' + url_params['code'] +
                                '&grant_type=' + url_params['grant_type']
                                 )
        json_response = access_token_response.content.decode()
        result = json.loads(json_response)
        access_token = result['access_token']
        openid = result['openid']
        userinfo_response = requests.get('https://api.weixin.qq.com/sns/userinfo?' +
                                        'access_token=' + access_token +
                                        '&openid=' + openid +
                                        '&lang=zh_CN'
                                        )
        json_response = userinfo_response.content.decode()
        result = json.loads(json_response)
        openid = result["openid"]
        headimgurl = result["headimgurl"]
        all_logos = Logos.objects.all().order_by('-vote_nums')
        voter_set = WXVoters.objects.filter(openid=openid)
        all_ballots = Ballots.objects.all()
        if voter_set:
            voter = voter_set[0]
        else:
            voter = WXVoters()
            voter.openid = openid
            voter.headimgurl = headimgurl
            voter.save()
        return render(request, 'index.html', {
            "openid": voter.openid,
            "all_logos": all_logos,
            "all_ballots": all_ballots
        })