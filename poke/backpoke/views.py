from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, QueryDict
from django.core.serializers.json import DjangoJSONEncoder
import json
from backpoke.apps import *

# Create your views here.
class Evolution_Chains(View):
    def get(self, request, *args, **kwargs):
        data = BackEvolution(kwargs)
        respose = data.get_evolution()
        return HttpResponse(json.dumps(respose, cls=DjangoJSONEncoder), content_type='application/json')

class Details_Pokemon(View):
    def get(self, request, *args, **kwargs):
        data = BackEvolution(kwargs)
        respose = data.details_pokemon()
        return HttpResponse(json.dumps(respose, cls=DjangoJSONEncoder), content_type='application/json')
