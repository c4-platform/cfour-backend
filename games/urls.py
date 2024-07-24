from django.urls import path

from games.views import *

urlpatterns = [
    path('', GameList.as_view()),
    path('create/', GameCreateView.as_view()),
    path('<int:pk>/delete/', GameDeleteView.as_view()),
    path('<int:pk>/update/', GameUpdateView.as_view()),
    path('<int:pk>/', GameDetailView.as_view())
]
