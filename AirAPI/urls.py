from django.urls import path
from .views import air_quality_data, receive_sensor_data


urlpatterns = [
    path('air-quality/', air_quality_data, name='air_quality_data'),
    path('sensor-data/', receive_sensor_data, name='sensor-data'),
]
