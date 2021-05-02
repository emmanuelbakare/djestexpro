from estate.api.serializers import EstateSerializer
from estate.models import Estate
from rest_framework import generics, status
from rest_framework.response import Response

class EstateListCreateView(generics.ListCreateAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer

    def perform_create(self, serializer, pk=None):
        serialize=serializer.save()
        print('serialized ',serialize)
        estate=Estate.objects.get(id=serialize.id)
        print('new Estate ',estate)
        cuser=self.request.user
        estate.admin.add(cuser)
        
        # serialize.set(user=self.request.user)

        # current_user=self.request.user.id
        # print('Estate ', serialize.id)
        # print('Current User', current_user)
        # if current_user and serialize:
        #     admin=EstateAdmin.objects.create(estate=serialize)
        

        # print('perform create was implemented', esta)
        # return Response("Estate : "+ estate.name + " Current User : ",current_user)
        


def createEstate(self, request):
    # request
    newEstate=Estate(
                name="",
                total_house = "", 
                street1="", 
                city="",
                state_region="",
                country="",
                comment=""
            )
        
    

class EstateRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Estate.objects.all()
    serializer_class=EstateSerializer





