from django.urls import path, include 
from resident.api.views import ResidentViewSet  
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',ResidentViewSet )

app_name="resident"
urlpatterns = [
    path('', include(router.urls))
    # path('', AccountListCreateView.as_view(), name="list"),
    # path('<int:pk>/', AccountRUDView.as_view(), name="detail"),
]