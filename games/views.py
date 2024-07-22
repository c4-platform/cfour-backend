from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from games.models import Game
from games.serializers import GameSerializer


# Create your views here.


class ListGames(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=200)


class CreateGame(CreateAPIView):
    def create(self, request, *args, **kwargs):
        pass
