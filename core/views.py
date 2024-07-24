from rest_framework import status
from rest_framework.response import Response
from .models import File
from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def get_file_details(request, pk):
    file = File.objects.all()
    return Response(data=file, status=status.HTTP_200_OK)
