from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from assignmnet.permission import IsOwnerOnlyOrReadOnly
from product.models import Event
from product.serializers import EventSerializer


class ProductApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        events = EventSerializer(Event.objects.all(), many=True).data
        return Response(events, status=status.HTTP_200_OK)

    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response({"msg": "Event가 작성되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, obj_id):
        event = Event.objects.filter(id=obj_id)
        event_serializer = EventSerializer(event, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)