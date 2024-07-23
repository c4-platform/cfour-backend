from django.urls import path

from games.views import *

urlpatterns = [
    path('', ListGames.as_view()),
    path('create/', CreateGameView.as_view())
]
