from rest_framework import serializers

from product.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "explanation", "effective_date", "expiration_date"]



