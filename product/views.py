from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from assignmnet.permission import IsOwnerOnlyOrReadOnly
from product.models import Event
from product.serializers import EventSerializer


class ProductApiView(APIView):
    permission_classes = []

    def get(self, request):
        events = EventSerializer(Event.objects.all(), many=True).data
        return Response(events, status=status.HTTP_200_OK)

    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response({"msg": "Event가 작성되었습니다."}, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)