from django.db import models

# Create your models here.

class EvolutionChains(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=500,blank=True)
	height = models.CharField(max_length=500,blank=True)
	evolution_details = models.TextField(blank=True,null=True)
	evolves_to = models.TextField(blank=True,null=True)
	evolutions = models.TextField(blank=True,null=True)
	base_stats = models.TextField(blank=True,null=True)
	weight = models.CharField(max_length=500,blank=True)
	id_pokemon = models.CharField(max_length=500,blank=True)
	creation_date = models.DateTimeField(auto_now_add=True)
