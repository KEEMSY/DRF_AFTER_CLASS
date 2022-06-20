from datetime import datetime

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
        fields = ["explanation", "price", "expiration_date", "active"]

    def validate(self, data):
        if data.get("expiration_date") < datetime.now():
            raise serializers.ValidationError(
                detail={"error": "상품을 등록할 수 없습니다."}
            )
        return data

    def create(self, validated_data):
        explanation = validated_data.pop("explanation")
        explanation += str(f'\n {datetime.now()}에 등록된 상품입니다.')
        validated_data.add(explanation)

        product = Product(**validated_data)
        product.save()

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "explanation":
                explanation = instance.pop("explanation")
                updated_explanation = str(f'{datetime.now()}에 수정되었습니다.\n') + explanation
                instance.add(updated_explanation)
                continue

            setattr(instance, key, value)
        instance.save()


