from django.db.models import Avg
from django.utils import timezone
from rest_framework import serializers

from product.models import Event, Product, Review


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "explanation", "effective_date", "expiration_date", "active"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["content", "grade", "user", "product"]


class ProductSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()

    def get_review(self, obj):
        reviews = obj.review_set
        return {
            "last_review": ReviewSerializer(reviews.last()).data,
            "avg_grade": reviews.aggregate(avg=Avg("grade"))["avg"]
        }

    class Meta:
        model = Product
        fields = ["explanation", "price", "expiration_date", "active", "review"]

    def validate(self, data):
        if data.get("expiration_date") < timezone.now():
            raise serializers.ValidationError(
                detail={"error": "날짜를 확인 해 주세요."}
            )
        return data

    def create(self, validated_data):
        validated_data["explanation"] += str(f'\n\n{timezone.now()}에 등록된 상품입니다.')
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            if key == "explanation":
                value = str(f'{timezone.now()}에 수정되었습니다.\n\n') + value

            setattr(instance, key, value)
        instance.save()
        return instance
