==========COMMON REST FRAMEWORK IMPORTS========================
from rest_framework.decorators import action # for adding extra entpoint using a method in a viewset class 
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser #allow image, JSON parsin
from rest_framework.authtoken.models import Token  # get the authtoken model
from rest_framework.authentication import TokenAuthentication  # toke authentication
from rest_framework.permissions import IsAuthenticated # get Authenticated methods
from rest_framework.response import Response # return response in a view
from rest_framework import generics, status, viewsets, mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters


==============GenericAPIView ==================


from rest_framework  import generics
from rest_framework import mixins

class EbookListCreateAPIView (mixins.ListModelMixin,
				mixin.CreateModelMixin,
				generics.GenericAPIView):

	queryset =Ebook.objects.all()
	serializer_class=EbookSerializer

	def get(self, request,*args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request,*args, **kwargs):
		return self.create(request,*args, **kwargs)

or
===============CONCRETEVIEW===========CALLING PERFORM_CREATE
from rest_framework import generics
# for list and create of view api as above
class EbookListCreateAPIView(generics.ListCreateAPIView):
	queryset=Ebook.objects.all()
	serializer_class=EbookSerializer

# for update, delete
class EbookDetailsAPIView(generics. retrieveUpdateDestroyAPIView):
	queryset=Ebook.objects.all()
	serializer_class=EbookSerializer

#for creating Review model 

class ReviewCreateAPIView(generics.CreateAPIView):
	queryset= Review.objects.all()
	serializer_class=ReviewSerializer
	
	# to create a review object (that has a foreign key called ebook) you need to specify which ebook it belongs to 
	# after implementing this method instead of fields="__all__ in ReviewSerialiser class use exclude="ebooks"
	# this excludes the ebook field while creating a new review for the specifed ebook
	def perform_create(self, serializer):
		ebook_pk=self.kwargs.get("pk")   # retrieve the id of the ebook as passed into the url e.g http://localhost:8000/books/1/review	
		ebook=get_object_or_404(Ebook, pk=ebook_pk) #retrieve the specific ebook whose Review model we want to create add "from rest_framework.generics import get_object_or_404" to use it
		serializer.save(ebook=ebook)  # save the  serialized object


#
=====mixins==================================================================
rest_framework import mixins
rest_framework import generics

mixins.ListModelMixin		def get    --return self.list(self,request, *args,**kwargs)
mixins.RetrieveModelMixin	def get	   -- return self.retrieve(
mixins.CreateModelMixin		def create -- return self.post(
mixins.UpdateModelMixin		def put    --return self.update(
mixins.UpdateModelMixin    	def patch   -- return self.partial_update(
mixins.DeleteModelMixin		def delete  -- returns self.destroy


post:create
get:retrieve
put:update
get:list
delete:destroy

CRULD
e.g

class BookListCreate(mixin.ListModelMixin, 
                    mixin.CreateModelMixin,
                    generics.GenericAPIView):
	queryset= Book
	serializer_class=BookSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)	

	def create(request, *args, **kwargs):
		return self.post(request, *args, **kwargs)

=============================================================================

MODEL VIEWSETS

from  rest_framework import viewsets
from ebooks.models import Ebook
from ebooks.api.serializer import EbookSerializer

class EbookViewsets(viewsets.ModelViewSet):
    queryset= Ebook.objects.all()
    serializer_class = EbookSerializer

=========== IN THE URLS SET THE router==================

from django.urls import path, include
from rest_framework import routers
from ebooks.api.apiViewSet import EbookViewsets

router= routers.DefaultRouter()
router.register('books', EbookViewsets)

urlpatterns =[
    path('',include(router.urls)),
]


--- FOR CUSTOMER VIEWSET USE SimpleRouter instead of Default Router to add multiple url endpoints ===============
from django.urls import path, include
from rest_framework import routers
from ebooks.api.apiViewSet import EbookViewsets

router= routers.SimpleRouter()
router.register('books', EbookViewsets)
router.register('registeredPeople', GetRegisteredViewSets)

urlpatterns =[
    path('',include(router.urls)),
]





# ================PERMISSION CLASS=================================
# ADD this to settings.py if the permission is same across all files. e.g. everyone must be authenticated before access

REST_FRAMEWORK={
	'DEFAULT_PERMISSION_CLASSES:{
		'rest_framework.permissions.IsAuthenticatedorReadOnly
    }
}


# ============================UPDATING NESTED RECORD ===============================
#using viewset the code below give us an endpoint of http://localhost:8000/api/accounts/
# which list all user data (username, email, profile) the profile is another model that is nested 
#views.py
class AccountViewsets(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=AccountSerializer
    parser_classes = (JSONParser,FormParser,MultiPartParser)


#serializers.py
class ProfileSerializer(serializers.ModelSerializer):
    profile_pic=serializers.ImageField(use_url=True, max_length=None)
    class Meta:
        model = Profile
        fields = ('firstname','lastname','phone','profile_pic', )

class AccountSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    class Meta:
        model= get_user_model()
        fields=('email','username','profile')

# example of result using http://localhost:8000/api/accounts/2/

{
    "email": "admin2@email.com",
    "username": "admin2",
    "profile": {
        "firstname": "Michael",
        "lastname": "Ayodeji",
        "phone": "08035485437",
        "profile_pic": "http://localhost:8000/media/profile_pix/net5.jpg"
    }
}
*****************************MODELVIEWSET ACTION*********************************************
#to update the profile data using  http://localhost:8000/api/accounts/2/profile, you will have to a method (def profile(self,request,pk=None)) under ActionViewsets that takes the request and serializer it with ProfileSerializer (The nested model) and save it. then returns a response.

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class AccountViewsets(viewsets.ModelViewSet):
    queryset= User.objects.all()
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


----------------------another modelViewset action example---------------------------------------------
class PollViewset(viewsets.ModelViewSet):
    serializer_class=QuestionSerializer
    queryset= Question.objects.all()
    lookup_field='id'

    #  use question/12/choices to get question choices
    @action(detail=True, methods=['GET']):
    def choices(self, request, id=None):
        question = self.get_object()  # get the class queryset object -question
        choices = Choice.objects.filter(question=question)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=200)

    # use question/12/choice to post a new choice
    @action (detail=True, methods=['POST'])
    def choice(self, request,id=None):
        question=self.get_object()
        data=request.data
        data['question']=question.id
        serializer = ChoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
