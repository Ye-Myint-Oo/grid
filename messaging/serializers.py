from rest_framework import serializers
from .models import QueueMessage

class QueueMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueMessage
        fields = '__all__'