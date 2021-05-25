from estate.api.serializers import (EstateSerializer, EstateAdminSerializer, 
                                      EstateTypeSerializer, EstateResidentSerializer)
from estate.models import Estate, EstateAdmin, EstateType
from resident.models import Resident
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

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
        print('ALL REQUEST', request)
        print('ALL REQUEST DATA ', request.data)
        account_dict=request.data.pop('account')
        resident_dict=request.data.pop('resident')
        estate_dict=request.data.pop('estate')
        print('RESIDENT', resident_dict)
        print('REMAINING REQUEST ', request.data)
        print('ACCOUNT', account_dict)
        print('ESTATE', estate_dict)

        estate = Estate(**estate_dict)
        print('CREATED ESTATE ', estate)
        user=self.request.user
        sa=EstateAdmin(user=user, estate=estate )

        print('CREATED ESTATE ADMIN ', sa)
        # save the data after creating them
        Resident.create(**resident_dict)



        estate.save()
        sa.save()
        
        
        # if bool(user['first_name']):
        #     user.first_name=account_dict['first_name']
        #     user.last_name=account_dict['last_name']

        # If there is no first name in the user add firstname as entered in the form
        if not bool(user.first_name):
            user.first_name=account_dict['first_name']

# If there is no first name in the user add firstname as entered in the form
        if not bool(user.last_name):
            user.last_name=account_dict['last_name']


        return Response(Estate)



        


       
        # create a new estate
        # return self.create(request,*args,**kwargs)
        # estate= self.create(request,*args,**kwargs)

        
        # #get the current user
        # user=self.request.user
        # print('NEW USER', user,' NEW USER FIRST NAME :: ', user.first_name)
        # #create an Estate Admin using user and estate
        # admin=EstateAdmin.object.create(user=user, estate=estate)

        # print('NEW ADMIN ',admin)

        # # create the admin as a resident
        # resident['user']=user
        # resident['estate']=estate
        # new_resident=Resident(user=user, estate=estate)
        # print('NEW RESIDENT ',new_resident)
        

        

    

  

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
        # serialized.admins.create(user=self.request.user)  # get the saved data and add
        EstateAdmin.objects.create(user=self.request.user, estate=serialized)

class EstateResidentListCreateView(generics.ListCreateAPIView):
    queryset=Estate.objects.all()
    serializer_class = EstateResidentSerializer

    # def perform_create(self, serialized):
    #     print(serialized)


    

class EstateRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer





