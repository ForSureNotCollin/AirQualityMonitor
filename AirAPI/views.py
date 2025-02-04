from rest_framework.response import Response
from rest_framework.decorators import api_view

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
