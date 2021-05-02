from django.urls import path, include 
from accounts.api.views import AccountViewsets 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',AccountViewsets )

app_name="accounts"
urlpatterns = [
    path('', include(router.urls))
    # path('', AccountListCreateView.as_view(), name="list"),
    # path('<int:pk>/', AccountRUDView.as_view(), name="detail"),
]