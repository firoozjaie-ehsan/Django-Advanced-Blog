from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from rest_framework.authtoken.views import ObtainAuthToken
from .. import views

urlpatterns = [
    # registration
    path("registration/", views.RegistrationApiView.as_view(), name ="registration"),
    
    # test send email
    path('send_email/', views.TestEmailSend.as_view(), name ='send_email'),
    #activation
    # path("activation/confirm/"),
    
    #resend activation
    # path("activation/resend/"),
    
    #change password
    path("change_password", views.ChangePasswordView.as_view(), name="change_password"),
    
    #reset password
    
    #login token
    path('token/login/', views.CustomObtainAuthToken.as_view(), name ="token-login"),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name ="token-logout"),
    
    #login jwt
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name ="jwt-create"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]