from .models import Game
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from core.models import File


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CreateGameSerializer(Serializer):
    full_name = serializers.CharField(max_length=120, unique=True)
    description = serializers.CharField()
    background_image = serializers.ImageField()
    icon = serializers.ImageField()

    def create(self, validated_data):
        background_image = validated_data.pop('background_image')
        icon = validated_data.pop('icon')

        background_image_instance = File.objects.create(file=background_image)
        icon_instance = File.objects.create(file=icon)

        game = Game.objects.create(background_image=background_image_instance, icon=icon_instance, **validated_data)

        return game
