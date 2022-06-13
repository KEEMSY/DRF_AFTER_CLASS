from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from assignmnet.permission import IsOwnerOnlyOrReadOnly


class TestView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]


    # permission_classes = [IsOwnerOnlyOrReadOnly]
    def get(self, request):
        return Response({'msg': 'get method'}, template_name='userapp/login')

    def post(self, request):
        return Response({'msg': 'post method'})

    def put(self, request):
        return Response({'msg': 'put method'})

    def delete(self, request):
        return Response({'msg': 'delete method'})
