from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        data = {
            'msg': 'success!'
        }
        return Response(data)
