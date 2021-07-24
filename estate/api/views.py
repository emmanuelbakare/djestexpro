from estate.api.serializers import (EstateSerializer, EstateAdminSerializer, 
                                      EstateTypeSerializer, EstateResidentSerializer,
                                       OnboardingSerializer,OnboardingListSerializer)
from resident.api.serializers import ResidentSerializer, MyResidentSerializer
from estate.models import Estate, EstateAdmin, EstateType, Onboarding 
from resident.models import Resident
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import action, parser_classes

class EstateTypeListCreateView(generics.ListCreateAPIView):
    queryset=EstateType.objects.all()
    serializer_class= EstateTypeSerializer


 
class EstateViewset(viewsets.ModelViewSet):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer
    filter_backends= (DjangoFilterBackend,OrderingFilter, SearchFilter)
    filter_fields=('status',)
    ordering=('created_date',)
    search_fields=('name', 'city', 'state_region', 'country',)
    parser_classes= (MultiPartParser, FormParser, JSONParser,)

    # list all the residents in the selected estate
    @action(detail=True , methods=['GET'])
    def residents(self, request, pk=None):
        estate=self.get_object()
        residents=Resident.objects.filter(estate=estate)
        sResidents=ResidentSerializer(residents, many=True)
        return Response(sResidents.data, status=200)

     
     
    @action(detail=True, methods=['GET'])
    def obList(self, request, pk=None):
        ob_list=self.get_object().onboarding.values('id','title').order_by('-id')
        serialized=OnboardingListSerializer(ob_list, many=True)
        return Response(serialized.data, status=200)

    @action(detail=True, methods=['GET','POST'])
    def onboarding(self, request, pk=None):
        if request.method=="GET":
            onboardings=self.get_object().onboarding.all() # get all onboardings for this estate
            serialized=OnboardingSerializer(onboardings, many=True)
            return Response(serialized.data, status=200)
        elif request.method=="POST":
 
            estate=self.get_object()
            data=request.data.copy() # request.data is immutable and cannot be modified - make a copy of it instead request.data.copy()
            print('REQUEST: ', data)
            data['estate']=estate.pk
            # if request.FILES:
 
            serialized = OnboardingSerializer(data=data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status=200)
            else:
                return Response(serialized.errors, status=401)



    # 'Resident(id, user, estate, house_address, status, created_date, comment)'
    # Add a new resident to an existing estate
    @action(detail=True, methods=['POST'])
    def resident(self,request, pk=None):
        estate=self.get_object()
        user=request.user
        data=request.data
        data['user']=user.pk
        data['estate']=estate.pk
        serializer=ResidentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)



class EstateAdminAPIView(generics.ListCreateAPIView):
    queryset=EstateAdmin.objects.all()
    serializer_class= EstateAdminSerializer
 


class CreateEstateAdminAPIView(mixins.CreateModelMixin, 
                               generics.GenericAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer

   
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

# class EstateResidentListCreate(generics.ListCreateAPIView):
#     # queryset=Resident.objects.all()
#     serializer_class= MyResidentSerializer

#     def get_queryset(self):
#         estate_id=self.kwargs.get('pk')
#         queryset =Resident.objects.filter(estate_id=estate_id)
#         return queryset
#         # serialized=ResidentSerializer(resident, many=True)
#         # return Response(serialized.data)
#     # Resident(id, user, estate, house_address, status, created_date, comment)
#     def perform_create(self, serialized):
#         user=self.request.user
#         data=serialized.data
#         serialized.save()

# class EstateResidentListCreate2(mixins.CreateModelMixin, 
#                                mixins.ListModelMixin, 
#                                generics.GenericAPIView):
#     serializer_class= MyResidentSerializer
#     queryset= Resident.objects.all()

#     def get(self, request, *args, **kwargs):
#         # self.list( request, *args, **kwargs)
#         estate_id=self.kwargs.get('pk')
#         resident =Resident.objects.filter(estate_id=estate_id)
#         serialized_resident=MyResidentSerializer(resident, many=True)
#         return Response(serialized_resident.data)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
         




    
# class EstateRUDView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Estate.objects.all()
#     serializer_class=EstateSerializer




class OnboardingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset= Onboarding.objects.all()
    serializer_class= OnboardingSerializer
 
    
