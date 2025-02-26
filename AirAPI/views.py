from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import requests 
from django.http import JsonResponse
from django.conf import settings

# for testing
@api_view(['GET']) 
def air_quality_data(request):
    """
    API endpoint to fetch air quality data
    """
    sample_data = {
        "location": "New York",
        "AQI": 42,
        "status": "Good"
    }
    return Response(sample_data)


@swagger_auto_schema(
    method='post',
    request_body=SensorDataSerializer,
    responses={
        201: openapi.Response("Data saved successfully"),
        400: openapi.Response("Validation error")
    },
)

@api_view(['POST'])
def receive_sensor_data(request):
    serializer = SensorDataSerializer(data=request.data)

    if serializer.is_valid(): 
        serializer.save()
        return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_weather(request):
    city = "Milwaukee"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=imperial"
    
    response = requests.get(url)
    data = response.json()

    return JsonResponse({
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    })