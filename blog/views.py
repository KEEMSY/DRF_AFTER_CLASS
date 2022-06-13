from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.permission import CanWriteAfter3Days, CanWriteAfter3Min


class ArticleApiView(APIView):
    permission_classes = [CanWriteAfter3Days]

    def post(self, request):
        title = request.data.get('title', '')
        content = request.data.get('content', '')
        category = request.data.get('category', '')
        return Response({"message": "게시글이 작성되었습니다."}, status=status.HTTP_200_OK)


class TestArticleApiView(APIView):
    permission_classes = [CanWriteAfter3Min]

    def post(self, request):
        title = request.data.get('title', '')
        content = request.data.get('content', '')
        category = request.data.get('category', '')
        return Response({"message": "게시글이 작성되었습니다."}, status=status.HTTP_200_OK)
