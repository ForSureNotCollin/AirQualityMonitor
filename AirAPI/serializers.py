from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    # Define required fields explicitly
    co2 = serializers.FloatField(required=True)
    humidity = serializers.FloatField(required=True)
    pm1_0 = serializers.FloatField(required=False, allow_null=True)
    pm2_5 = serializers.FloatField(required=False, allow_null=True)
    pm10_0 = serializers.FloatField(required=False, allow_null=True)
    temperature = serializers.FloatField(required=True)

    class Meta:
        model = SensorData
        fields = '__all__' 
