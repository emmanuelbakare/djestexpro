from django.urls import path, include 
from estate.api.views import (  EstateViewset,EstateAdminAPIView,CreateEstateAdminAPIView,
                                 EstateTypeListCreateView,OnboardingDetails ) 
                                 
from rest_framework import routers

router=routers.DefaultRouter()
# router.register('',EstateAdminViewSet)
router.register('', EstateViewset)

app_name="estates"
urlpatterns = [
    path('admin/', EstateAdminAPIView.as_view(), name="estate-admin"),
    path('type/', EstateTypeListCreateView.as_view(), name="type"),
    path('onboarding/<int:pk>/', OnboardingDetails.as_view(), name="ob-details"),

    path('', include(router.urls), name="estates"),
    # path('resident/', EstateResidentListCreateView.as_view(),name='estate-resident'),
    path('resident/', CreateEstateAdminAPIView.as_view(),name='estate-resident'),
    # path('<int:pk>/', EstateRUDView.as_view(), name="detail"),
    # path('<int:pk>/residents/', EstateResidentListCreate2.as_view(), name="estate-residents"),
   
]