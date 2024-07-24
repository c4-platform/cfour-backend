from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from games.models import Game
from rest_framework import status

from games.serializers import CreatedGameSerializer, CreateGameSerializer, GameSerializer, GameDetailsSerializer, \
    UpdateGameSerializer


# Create your views here.


class GameList(ListAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameCreateView(CreateAPIView):
    serializer_class = CreateGameSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateGameSerializer(data=request.data)
        if serializer.is_valid():
            game = serializer.save()
            serialized_game = CreatedGameSerializer(game).data
            return Response(serialized_game, status=status.HTTP_201_CREATED)


class GameUpdateView(UpdateAPIView):
    serializer_class = UpdateGameSerializer

    def update(self, request, *args, **kwargs):
        serializer = UpdateGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetailView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailsSerializer


class GameDeleteView(DestroyAPIView):
    queryset = Game.objects.all()
