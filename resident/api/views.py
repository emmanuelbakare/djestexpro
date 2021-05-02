from resident.api.serializers import ResidentSerializer
from resident.models import Resident
from rest_framework import viewsets

class ResidentViewSet(viewsets.ModelViewSet):
    queryset=Resident.objects.all()
    serializer_class=ResidentSerializer


