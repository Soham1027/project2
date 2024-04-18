from urllib import response
from django import views
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from project2.settings import SECRET_KEY
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken  # type:ignore
from django.db.models import Q

from django.shortcuts import get_object_or_404
import jwt  # type: ignore

from .models import (
    UserDatas,
    Players,
    Coaches,
    CourtDetails,
    Profiles,
    Addresses,
    GroundProviders,

)
from .serializer import (
    ProfileSerializer,
    UserSerializer,
    UserLogoutSerializer,

    
    CourtDetailSerializer,
   
    GroundProviderSerializer,
    TestAddressSerializer,
    TestProfileSerializer,

    LoginSerializer,
    UpdateUserSerializer,

   
    CreateUpdateGroundProviderSerializer,
    CreateUpdateCourtDetailSerializer,

)


# Create your views here.

##########USER##########

class UserView(APIView):
    serializer_class = UserSerializer

    def post(self, request):

        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            email_exists = UserDatas.objects.filter(email=data['email']).exists()
            if email_exists:
                response = {"status": 400, "message": "Email Exists"}
            else:
                serializer.save()
                response = {"status": 200, "message": "User Register"}
            return redirect('login')

        return Response(serializer.errors)

    def get(self, request):

        response = {'status': 200}
        player_objs = UserDatas.objects.all()
        serializer = UserSerializer(player_objs, many=True)
        response['data'] = serializer.data  # type: ignore

        return Response(response)
    
    
    def patch(self, request, *args, **kwargs):

        response = {'status': 200}
        data = request.data
        try:
            obj = UserDatas.objects.get(id=data.get('id'))
            serializer = UpdateUserSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data  # type: ignore
                return Response(response)
            else:
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': 'invalid id'})


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')

        try:
            user = UserDatas.objects.get(email=email)
            print(password)
            print(user.password)

        except UserDatas.DoesNotExist:
            return Response({'error': 'Invalid'}, status=400)

        if not check_password(password, user.password):
            print(password)
            print(user.password)
            return Response({'error': 'Password Invalid'}, status=400)

        if role != user.role:
            return Response({'error': 'Role Not match'}, status=400)

        refresh = RefreshToken.for_user(user)

        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        serializer = UserSerializer(user)

        return Response({'token': token, 'user': serializer.data})


class LogoutView(APIView):
    serializer_class = UserLogoutSerializer

    def post(self, request):
        logout(request)

        return redirect('login')


###########PROFILE##########


class TestProfileDetailView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()

    serializer_class = TestProfileSerializer

    def get_queryset(self):

        user = self.request.META['HTTP_USER_ID']
        print("sdfjgsdh", user)
        user_data = UserDatas.objects.filter(id=user).first()
        print(user_data)
        if user_data:
            if user_data.role == "Player":
                queryset = self.queryset.exclude(player__isnull=True)
                print(queryset)
            elif user_data.role == "Coach":
                queryset = self.queryset.exclude(coach__isnull=True)
                print("asdfasd", queryset)

            return queryset

    # (player__isnull=True))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class TestProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = TestProfileSerializer




########### Ground Provider Profile##########

class ProfileDetailView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()

    serializer_class = ProfileSerializer

  

  


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializer



########### Ground Provider ##########

class GroundProviderView(APIView):
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]

    serializer_class = CreateUpdateGroundProviderSerializer

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        ground_provider_objs = GroundProviders.objects.all()
        serializer = GroundProviderSerializer(ground_provider_objs, many=True)
        response['data'] = serializer.data  # type: ignore

        return Response(response)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CreateUpdateGroundProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Ground Data Added"}
            return Response(response)

        return Response(serializer.errors)

class GroundProviderUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroundProviders.objects.all()
    serializer_class = CreateUpdateGroundProviderSerializer


###########COURTDETAIl##########

class CourtDetailView(APIView):
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]

    serializer_class = CreateUpdateCourtDetailSerializer

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        court_details_objs = CourtDetails.objects.all()
        serializer = CourtDetailSerializer(court_details_objs, many=True)
        response['data'] = serializer.data  # type: ignore

        return Response(response)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CreateUpdateCourtDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Court Detail Data Added"}
            return Response(response)

        return Response(serializer.errors)

    def patch(self, request, *args, **kwargs):

        response = {'status': 200}
        data = request.data
        try:
            obj = CourtDetails.objects.get(id=data.get('id'))
            serializer = CreateUpdateCourtDetailSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data  # type: ignore
                return Response(response)
            else:
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': 'invalid id'})

    def delete(self, request, *args, **kwargs):
        response = {'status': 200}
        data = request.data
        try:
            obj = CourtDetails.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status': 200, 'message': "Deleted"})
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': "Invalid id"})
