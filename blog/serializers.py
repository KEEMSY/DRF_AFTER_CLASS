from rest_framework import serializers

from blog.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "bio"]


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = ["title", "content", "category"]



