from django.urls import path, include

from .. import views
urlpatterns = [
    #profile
    path('', include('accounts.api.v1.urls.accounts')),
    path('profile/', include('accounts.api.v1.urls.profiles')),
    
    
]