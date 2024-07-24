from django.urls import path
from .views import get_file_details

urlpatterns = [
    path('/<int:pk>/', get_file_details)
]
