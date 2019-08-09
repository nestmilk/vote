import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from ballots.models import Ballots
from logos.models import Logos
from voters.models import WXVoters


class IndexView(View):
    """
    投票界面
    """
    def get(self, request):
        all_logos = Logos.objects.all().order_by('vote_nums')
        return render(request, 'index.html', {
            "all_logos": all_logos,
        })

    def post(self, request):
        logo_ids_str = request.POST.getlist("logo_ids")
        openid = request.POST.get("openid")

        voter_set = WXVoters.objects.filter(openid=openid)
        if voter_set:
            voter = voter_set[0]
            ballot_set = Ballots.objects.filter(voter__openid=openid)
            for id in logo_ids_str:
                id = int(id)
                exit = False
                for ballot in ballot_set:
                    ballot_logo_id = ballot.logo.id
                    if ballot_logo_id == id:
                        exit = True
                        break
                if not exit:
                    ballot = Ballots()
                    logo = Logos.objects.filter(id=id)[0]
                    ballot.voter = voter
                    ballot.logo = logo
                    ballot.save()
                    logo.vote_nums += 1
                    logo.save()

        return HttpResponse(json.dumps({"status": "success"}), content_type="application/json")
