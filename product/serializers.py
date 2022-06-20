import pytz
from datetime import datetime

from django.utils import timezone
from rest_framework import serializers

from product.models import Event, Product


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "explanation", "effective_date", "expiration_date", "active"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["explanation", "price", "expiration_date", "active", "user"]

    def validate(self, data):
        if data.get("expiration_date") < timezone.now():
            raise serializers.ValidationError(
                detail={"error": "날짜를 확인 해 주세요."}
            )
        return data

    def create(self, validated_data):
        validated_data["explanation"] += str(f' {timezone.now()}에 등록된 상품입니다.')
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        print('instance: ', instance)

        for key, value in validated_data.items():
            print('key, value: ', key, value)
            if key == "explanation":
                value = str(f'{timezone.now()}에 수정되었습니다.') + value

            setattr(instance, key, value)
        instance.save()
        return instance

