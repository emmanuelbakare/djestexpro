from django.urls import path, include 
from estate.api.views import (EstateListCreateView, EstateRUDView, 
                                EstateAdminViewSet, EstateTypeListCreateView,
                                 CreateEstateAdminAPIView, EstateResidentListCreate2,  )
from rest_framework import routers

router=routers.DefaultRouter()
router.register('',EstateAdminViewSet)

app_name="estates"
urlpatterns = [
    path('admin/', include(router.urls), name="estate-admin"),
    path('', EstateListCreateView.as_view(), name="list"),
    path('type/', EstateTypeListCreateView.as_view(), name="type"),
    # path('resident/', EstateResidentListCreateView.as_view(),name='estate-resident'),
    path('resident2/', CreateEstateAdminAPIView.as_view(),name='estate-resident2'),
    path('<int:pk>/', EstateRUDView.as_view(), name="detail"),
    path('<int:pk>/residents/', EstateResidentListCreate2.as_view(), name="estate-residents"),
   
]