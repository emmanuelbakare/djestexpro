from django.urls import path, include


urlpatterns = [
    path('accounts/', include('accounts.api.urls')),
    path('estate/', include('estate.api.urls')),
    path('resident/', include('resident.api.urls')),
    
     
]
