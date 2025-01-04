from django.shortcuts import render

from rest_framework.views import APIView, Response

from .models import Pokemon

from move_app.models import Move

from django.core.serializers import serialize # DISCUSS WHAT THIS IS SHORTLY!!!!

import json

# Create your views here.

# RESTful API process:
    # request comes in
    # take data from request, turn into variables
    # access data in database - if constraints on data provided in request, apply those
    # get data back from databse
    # turn data into JSON format
    # return JSON data as Reponse

class AllPokemon(APIView):
    def get(self, request): # return all Pokemon in our database to the user/requester
    
        # get a list of all the Pokemon in our database

        all_pokemon = Pokemon.objects.order_by("name")
        
        # turn QuerySets into JSON-formatted binary string

        all_pokemon_serialized = serialize("json", all_pokemon)

        # turn JSON-formatted string into JSON

        all_pokemon_json = json.loads(all_pokemon_serialized)

        # return JSON data as Reponse

        return Response(all_pokemon_json)


class SelectedPokemon(APIView):
    #  Specify the method to trigger this behavior
    def get( self, request, id ): # <-- Notice id is now a parameter and its value is being pulled straight from our URL
        # Lets initialize pokemon as None and give it a
        # corresponding query set depending on the ids type
        pokemon = None
        # id is an int
        if type(id) == int:
            pokemon = Pokemon.objects.get(id=id)
        # id is a string
        else:
            pokemon = Pokemon.objects.get(name=id.title())
        # Since pokemon is a single instance it needs to be wrapped by [] to make it
        # iterable for the serialize function to turn it into a binary string
        json_pokemon = serialize("json", [pokemon])
        serialized_pokemon = json.loads(json_pokemon)[0] # <--We don't want our Pokemon data in a list
        # Grab a pokemons serialized moves data
        moves = json.loads(
            serialize(
                "json",
                Move.objects.filter(id__in=serialized_pokemon["fields"]["moves"]),
            )
        )
        serialized_pokemon["fields"]["moves"] = moves
        # return Response(unserialized_pokemon)
        return Response(serialized_pokemon)