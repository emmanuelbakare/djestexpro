from estate.api.serializers import EstateSerializer, EstateAdminSerializer, EstateTypeSerializer
from estate.models import Estate, EstateAdmin, EstateType
from resident.models import Resident
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class EstateTypeListCreateView(generics.ListCreateAPIView):
    queryset=EstateType.objects.all()
    serializer_class= EstateTypeSerializer

    

  

class EstateAdminViewSet(viewsets.ModelViewSet):
    queryset=EstateAdmin.objects.all()
    serializer_class= EstateAdminSerializer

    def perform_create(self, serializer, pk=None):
        print(serializer)
        # serializer.save()

class EstateListCreateView(generics.ListCreateAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer
    filter_backends= (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_fields=('status',)
    ordering=('created_date',)
    search_fields=('name', 'city', 'state_region', 'country',)

    def perform_create(self, serializer, pk=None):
        serialized=serializer.save()  # save the data
        # attach this user as admin on this created estate
        serialized.admins.create(user=self.request.user)  # get the saved data and add



    

class EstateRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer





