from django.urls import path

from .. import views

urlpatterns = [
    # profile
    path("", views.ProfileAPIView.as_view(), name="profile"),
]
