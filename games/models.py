from core.models import File
from django.db import models


# Create your models here.


class Game(models.Model):
    full_name = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    background_image = models.OneToOneField(File, related_name='game_background_image', on_delete=models.CASCADE)
    icon = models.OneToOneField(File, related_name='game_icon', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.full_name
