
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser,MultiPartParser, FormParser

from accounts.models import Profile
from accounts.api.serializers import ProfileSerializer, AccountSerializer
from django.contrib.auth import get_user_model

user=get_user_model()


class AccountViewsets(viewsets.ModelViewSet):
    queryset= user.objects.all()
    serializer_class=AccountSerializer
    parser_classes = (JSONParser,FormParser,MultiPartParser)

    @action(detail=True, methods=['PUT'])
    def profile(self, request, pk=None):
        user=self.get_object()
        profile=user.profile
        serializer=ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AccountListCreateView(generics.ListCreateAPIView):
#     queryset = user.objects.all()
#     serializer_class= AccountSerializer

# class AccountRUDView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = user.objects.all()
#     serializer_class= AccountSerializer