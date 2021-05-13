from django.urls import path, include 
from estate.api.views import (EstateListCreateView, EstateRUDView, 
                                EstateAdminViewSet, EstateTypeListCreateView, )
from rest_framework import routers

router=routers.DefaultRouter()
router.register('',EstateAdminViewSet)

app_name="estates"
urlpatterns = [
    path('admin/', include(router.urls), name="estate-admin"),
    path('', EstateListCreateView.as_view(), name="list"),
    path('type/', EstateTypeListCreateView.as_view(), name="type"),
    path('<int:pk>/', EstateRUDView.as_view(), name="detail"),
]