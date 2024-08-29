from rest_framework import generics
from django.core.mail import send_mail

from ...models import Profile
from .serializers import CustomAuthTokenSerializer, RegistrationSerializer,CustomTokenObtainPairSerializer, ChangepasswordSerializer,ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
User= get_user_model()
class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            data ={
                'email': serializer.validated_data['email'],
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class ChangePasswordView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangepasswordSerializer
    
    def get_object(self, query_set = None):
        obj = self.request.user
        return obj
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"details": "password changed successfully", "status": status.HTTP_200_OK})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
    

class TestEmailSend(generics.RetrieveUpdateAPIView):
    def get(self, request, *args, **kwargs):
        send_mail(
            "Subject here",
            "kiram to koset from ehsan django web.",
            "firoozjaieehsan@gmail.com",
            ["hodakarimirad82@gmail.com"],
            fail_silently=False,
        )
        return Response("email send")