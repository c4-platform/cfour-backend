from .models import Game
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from core.models import File


class CreatedGameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'full_name']


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'full_name', 'description']


class GameDetailsSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'full_name', 'description', 'background_image', 'icon']


class CreateGameSerializer(Serializer):
    full_name = serializers.CharField(max_length=120)
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


class UpdateGameSerializer(Serializer):
    full_name = serializers.CharField(max_length=120)
    description = serializers.CharField()
    background_image = serializers.ImageField(allow_null=True)
    icon = serializers.ImageField(allow_null=True)

    def create(self, validated_data):
        background_image = validated_data.pop('background_image')
        icon = validated_data.pop('icon')
        background_image_instance = File.objects.create(file=background_image)
        icon_instance = File.objects.create(file=icon)
        game = Game.objects.create(background_image=background_image_instance, icon=icon_instance, **validated_data)
        return game

    def update(self, instance, validated_data):
        print('--------')
        if 'background_image' in validated_data:
            print('-------------------------')
            background_image = validated_data.pop('background_image')
            background_image_instance = File.objects.create(file=background_image)
            instance.background_image = background_image_instance
        if 'icon' in validated_data:
            icon = validated_data.pop('icon')
            icon_instance = File.objects.create(file=icon)
            instance.icon = icon_instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
