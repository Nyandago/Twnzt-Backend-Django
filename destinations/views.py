from django.http import JsonResponse
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST', 'GET'])
def destinations_list(request, format=None):

    if request.method == 'GET':
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        


@api_view(['GET','PUT','DELETE'])
def destination_detail(request, id, format = None):

    try:
        destination = Destination.objects.get(pk=id)
    except Destination.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DestinationSerializer(destination)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DestinationSerializer(destination, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        destination.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
