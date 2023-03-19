from django.http import JsonResponse
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST', 'GET'])
def destinations_list(request):

    if request.method == 'GET':
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return JsonResponse({'destinations':serializer.data})
    
    if request.method == 'POST':
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        


@api_view(['GET','PUT','DELETE'])
def destination_detail(request):
    