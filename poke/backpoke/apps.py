from django.apps import AppConfig
import requests
from django.http import HttpResponse, QueryDict
from django.core.serializers.json import DjangoJSONEncoder
import json
import ast
from backpoke.models import *


class BackpokeConfig(AppConfig):
    name = 'backpoke'


class BackEvolution():
    def __init__(self,kwargs):
        self._request = kwargs
        self.respose = {'code':200,'data':None}
        self.save = {}

    def get_evolution(self):
        try:
            if self._request.get('id'):
                url = "https://pokeapi.co/api/v2/evolution-chain/{}/".format(self._request.get('id'))
                url_stats = "https://pokeapi.co/api/v2/pokemon/{}/".format(self._request.get('id'))
                url_evolutions = "https://pokeapi.co/api/v2/evolution-trigger/{}/".format(self._request.get('id'))

                response = requests.get(url)
                if response.status_code != 200:
                     self.respose = {'code':500,'data':'Ingrese otro id'}
                     return self.respose
                data = json.loads(response.text)


                self.save['name'] = data.get('chain').get('species').get('name')
                self.save['evolution_details'] = data.get('chain').get('evolution_details')
                self.save['evolves_to'] = data.get('chain').get('evolves_to')

                #base_stats
                response_stats = requests.get(url_stats)
                data_stats = json.loads(response_stats.text)

                self.save['base_stats'] = data_stats.get('stats')
                self.save['weight'] = data_stats.get('weight')
                self.save['height'] = data_stats.get('height')
                self.save['id_pokemon'] = self._request.get('id')

                #evolutions
                response_evolutions = requests.get(url_evolutions)
                data_evolutions = json.loads(response_evolutions.text)
                self.save['evolutions'] = data_evolutions

                evoluion_save = EvolutionChains.objects.update_or_create(**self.save)

                self.respose = {'data':data}
                return self.respose
            else:
                self.respose = {'code':500,'data':'Es necesario el id'}
                return self.respose
        except Exception as e:
            self.respose = {'code':500,'data':str(e)}
            return self.respose

    def details_pokemon(self):
        evoluion_data = EvolutionChains.objects.get(name__icontains='cater')
        data = {
            "name":evoluion_data.name,
            "id":evoluion_data.id,
            "evolutions":ast.literal_eval(evoluion_data.evolutions),
            "height":evoluion_data.height,
            "evolution_details":ast.literal_eval(evoluion_data.evolution_details),
            "base_stats":ast.literal_eval(evoluion_data.base_stats),

        }
        self.respose = {'data':data}
        return self.respose
