from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PestIncident
from .serializers import PestIncidentSerializer
class PestIncidentListView(APIView):
    def get(self, request):
        incidents = PestIncident.objects.all()
        serializer = PestIncidentSerializer(incidents, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PestIncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PestIncidentDetailView(APIView):
    def get(self, request, incident_id):
        try:
            incident = PestIncident.objects.get(incident_id=incident_id)
        except PestIncident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PestIncidentSerializer(incident)
        return Response(serializer.data)
    def put(self, request, incident_id):
        try:
            incident = PestIncident.objects.get(incident_id=incident_id)
        except PestIncident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PestIncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, incident_id):
        try:
            incident = PestIncident.objects.get(incident_id=incident_id)
        except PestIncident.DoesNotExist:
            return Response({'error': 'Incident not found'}, status=status.HTTP_404_NOT_FOUND)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
