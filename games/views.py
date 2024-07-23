from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from games.models import Game
from rest_framework import status

from games.serializers import GameSerializer, CreateGameSerializer


# Create your views here.


class ListGames(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=200)


class CreateGameView(CreateAPIView):
    serializer_class = CreateGameSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateGameSerializer(data=request.data)
        if serializer.is_valid():
            game = serializer.save()
            serialized_game = GameSerializer(game).data
            return Response(serialized_game, status=status.HTTP_201_CREATED)

# class DeleteGameView(APIView):
#     def delete(self,request):
