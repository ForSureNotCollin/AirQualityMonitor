from django.urls import path
from .views import air_quality_data

urlpatterns = [
    path('air-quality/', air_quality_data, name='air_quality_data'),
]
