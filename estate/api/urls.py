from django.urls import path 
from estate.api.views import EstateListCreateView, EstateRUDView

app_name="estates"
urlpatterns = [
    path('', EstateListCreateView.as_view(), name="list"),
    path('<int:pk>/', EstateRUDView.as_view(), name="detail"),
]