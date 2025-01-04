from django.shortcuts import render

from rest_framework.views import APIView, Response

from .models import Move

from django.core.serializers import serialize

import json

# Create your views here.

class AllMoves(APIView):
    def get(self, request):

        all_moves = Move.objects.all()

        all_moves_serialized = serialize("json", all_moves)

        all_moves_json = json.loads(all_moves_serialized)

        return Response(all_moves_json)

class FireMoves(APIView):
    def get(self, request):

        fire_moves = Move.objects.filter(id='2')

        fire_moves_serialized = serialize("json", fire_moves)

        fire_moves_json = json.loads(fire_moves_serialized)

        return Response(fire_moves_json)

class PsychicMoves(APIView):
    def get(self, request):

        psychic_moves = Move.objects.filter(id=1)

        psychic_moves_serialized = serialize("json", psychic_moves)

        psychic_moves_json = json.loads(psychic_moves_serialized)

        return Response(psychic_moves_json)

class SelectedMove(APIView):

    def get(self, request, name):
        move = serialize('json', [Move.objects.get(name = name.title())])
        move = json.loads(move)[0]
        return Response(move)