from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from django.urls import path

from .views import Evolution_Chains,Details_Pokemon

urlpatterns = [
    path('evolution/<int:id>/', Evolution_Chains.as_view(), name='evolution_chains'),
    path('pokemon/<str:name>/', Details_Pokemon.as_view(), name='details_pokemon'),
]
