from datetime import datetime

from django.contrib.auth.models import AnonymousUser

# Create your views here.
from django.utils import timezone
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Event, Product
from product.permissions import IsAuthenticatedANDWritableAfter3DaysOrReadOnly
from product.serializers import EventSerializer, ProductSerializer


class EventApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        events = Event.objects.filter(effective_date__lte=datetime.now(),
                                      expiration_date__gte=datetime.now(),
                                      active=True)
        valid_events = EventSerializer(events, many=True).data
        return Response(valid_events, status=status.HTTP_200_OK)

    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response({"msg": "Event가 작성되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, obj_id):
        event = Event.objects.get(id=obj_id)
        event_serializer = EventSerializer(event, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductApiView(APIView):
    permission_classes = [IsAuthenticatedANDWritableAfter3DaysOrReadOnly]

    def get(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            products = Product.objects.all()
            valid_products = ProductSerializer(products, many=True).data
            return Response(valid_products, status=status.HTTP_200_OK)
        else:
            products = Product.objects.filter(user_id=request.user.id,
                                              expiration_date__gte=timezone.now(),
                                              active=True)
            valid_products = ProductSerializer(products, many=True).data
            return Response(valid_products, status=status.HTTP_200_OK)

    def post(self, request):
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({"msg": "Product가 작성되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, obj_id):
        product = Product.objects.get(id=obj_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


