from django.urls import path, include

from .. import views
urlpatterns = [
    #profile
    path('', views.ProfileAPIView.as_view(), name="profile"),
    
]