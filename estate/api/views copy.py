from estate.api.serializers import (EstateSerializer, EstateAdminSerializer, 
                                      EstateTypeSerializer, EstateResidentSerializer)
from resident.api.serializers import ResidentSerializer, MyResidentSerializer
from estate.models import Estate, EstateAdmin, EstateType
from resident.models import Resident
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import action

class EstateTypeListCreateView(generics.ListCreateAPIView):
    queryset=EstateType.objects.all()
    serializer_class= EstateTypeSerializer


class CreateEstateAdminAPIView(mixins.CreateModelMixin, 
                               mixins.ListModelMixin, 
                               generics.GenericAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer

    def get(self, request, *args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request, *args,**kwargs):
        # get all the request.data into a dictionary
        account_dict=request.data.pop('account')
        resident_dict=request.data.pop('resident')
        estate_dict=request.data
        # estate_dict=request.data.pop('estate')

        estate = Estate(**estate_dict)
        user=request.user
        admin=EstateAdmin(user=user, estate=estate)

        estate.save()
        admin.save()

        # add user and estate to resident dictionary since resident model requires it
        resident_dict['user']=user
        resident_dict['estate']=estate
        resident=Resident(**resident_dict) # create resident
        resident.status=1 # make this resident active
        resident.save()
        
        
       
        if not bool(user.first_name):
            print('FIRSTNAME IS EMPTY')
            user.first_name=account_dict['first_name']

# If there is no first name in the user add firstname as entered in the form
        if not bool(user.last_name):
            user.last_name=account_dict['last_name']
        
        user.save()

        serialized_estate=EstateSerializer(estate)
        return Response(serialized_estate.data)


        

class EstateAdminViewSet(viewsets.ModelViewSet):
    queryset=EstateAdmin.objects.all()
    serializer_class= EstateAdminSerializer



class EstateListCreateView(generics.ListCreateAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer
    filter_backends= (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_fields=('status',)
    ordering=('created_date',)
    search_fields=('name', 'city', 'state_region', 'country',)

    def perform_create(self, serializer, pk=None):
        serialized=serializer.save()  # save the data
        EstateAdmin.objects.create(user=self.request.user, estate=serialized)

class EstateResidentListCreate(generics.ListCreateAPIView):
    # queryset=Resident.objects.all()
    serializer_class= MyResidentSerializer

    def get_queryset(self):
        estate_id=self.kwargs.get('pk')
        queryset =Resident.objects.filter(estate_id=estate_id)
        return queryset
        # serialized=ResidentSerializer(resident, many=True)
        # return Response(serialized.data)
    # Resident(id, user, estate, house_address, status, created_date, comment)
    def perform_create(self, serialized):
        user=self.request.user
        data=serialized.data
        serialized.save()

class EstateResidentListCreate2(mixins.CreateModelMixin, 
                               mixins.ListModelMixin, 
                               generics.GenericAPIView):
    serializer_class= MyResidentSerializer
    queryset= Resident.objects.all()

    def get(self, request, *args, **kwargs):
        # self.list( request, *args, **kwargs)
        estate_id=self.kwargs.get('pk')
        resident =Resident.objects.filter(estate_id=estate_id)
        serialized_resident=MyResidentSerializer(resident, many=True)
        return Response(serialized_resident.data)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
         

 
   
 

# class EstateResidentListCreateView(generics.ListCreateAPIView):
#     queryset=Estate.objects.all()
#     serializer_class = EstateResidentSerializer

#     def perform_create(self, serialized):
#         print(serialized)


    
class EstateRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer





