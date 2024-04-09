
from base64 import decode
from django.http import JsonResponse
from django.shortcuts import render,redirect
from jwt import InvalidTokenError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,logout
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken  #type:ignore
from rest_framework_simplejwt.authentication import JWTAuthentication   #type:ignore
from django.shortcuts import get_object_or_404
 



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
    UserSerializer,
    UserLogoutSerializer,
    
    PlayerSerializer,
    CoachSerializer,
    CourtDetailSerializer,
    ProfileSerializer,
    AddressSerializer,
    GroundProviderSerializer,
    TestAddressSerializer,
    TestProfileSerializer,
 
 
    LoginSerializer,

    
    CreateUpdateAddressSerializer,
    CreateUpdateProfileSerializer,
    CreateUpdatePlayerSerializer,
    CreateUpdateCoachSerializer,
    CreateUpdateGroundProviderSerializer,
    CreateUpdateCourtDetailSerializer,
 
  
    
)

# Create your views here.

##########USER##########

class UserView(APIView):
    serializer_class=UserSerializer
    

    def post(self,request):
    
        data=request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            email_exists=UserDatas.objects.filter(email=data['email']).exists()
            if email_exists:
                response={"status":400,"message":"Email Exists"}
            else:
                serializer.save()
                response={"status":200,"message":"User Register"}
            return redirect('login')
        
        return Response(serializer.errors)
    def get(self,request):  
        
            response ={'status':200}
            player_objs=UserDatas.objects.all()
            serializer=UserSerializer(player_objs,many=True)
            response['data']=serializer.data # type: ignore
            
            return Response(response)

    



class LoginView(APIView):
    permission_classes = [AllowAny,]

    serializer_class=LoginSerializer
    
    def post(self, request,*args, **kwargs):
        email=request.data.get('email')
        password=request.data.get('password')
        role=request.data.get('role')
        
        try:
            users=UserDatas.objects.get(email=email)
            print(password)
            print(users.password)
          
        except UserDatas.DoesNotExist:
            return Response({'error':'Invalid'},status=400)
        
        if not check_password(password,users.password):
            print(password)
            print(users.password)
            return Response({'error':'Password Invalid'},status=400) 
           
        if role!=users.role:
               return Response({'error':'Role Not match'},status=400)    
        
       
          
          
        refresh=RefreshToken.for_user(users)
      
        token={
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
        
        serializer=UserSerializer(users)
      
        return Response({'token':token,'data':serializer.data})

  
class LogoutView(APIView):
    serializer_class=UserLogoutSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            logout(request)
            return redirect('login')
        except Exception as e:
            return Response(status=400)
        
   
      
        
  


class TestToken(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request, *args, **kwargs):
        # try:
        token = request.headers['Authorization'].split(' ')[1] 
        print(token)
        #     decoded_token = decode(token, 'your_secret_key', algorithms=['HS256']) # type: ignore
        #     user_id = decoded_token['user_id']  # Extract user_id from decoded token
        #     user = UserDatas.objects.get(id=user_id)  # Get user object using user_id
        #     # You can perform additional checks or operations here if needed
        #     return Response("Authorized", status=200)
        # except KeyError:
        #     return Response("Token not provided", status=400)
        # except InvalidTokenError:
        #     return Response("Invalid token", status=400)
        # except UserDatas.DoesNotExist:
        #     return Response("U not found", status=400)
  

# class TestProfileDetailView(APIView):  
  

class TestProfileDetailView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = TestProfileSerializer


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = TestProfileSerializer
    
    
               
            
                    

           
            
            
     
class ProfileDetailView(APIView):
  
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]
    # serializer_class = CreateUpdateProfileSerializer 
    # address_serializer_class=CreateUpdateAddressSerializer 
    
    def get(self, request, *args, **kwargs):
       
     
        response ={'status':200}
        profile_objs=Profiles.objects.all()
        serializer=ProfileSerializer(profile_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
 
    def post(self, request, *args, **kwargs):
        
          
        data=request.data
        serializer=CreateUpdateProfileSerializer(data=data)
        address_serializer=CreateUpdateAddressSerializer(data=data)
        if serializer.is_valid() or address_serializer.is_valid():
      
            serializer.save()
            address_serializer.save()
            
            response={"status":200,"message":"Profile Data Added"}
            return Response(response)
        
        
        
        
    
        # data=request.data
        # address_serializer=CreateUpdateAddressSerializer(data=data)
        # if address_serializer.is_valid():
      
        #     address_serializer.save()
        #     response={"status":200,"message":"Address Data Added"}
        #     return Response(response)
        
        
        return Response(serializer.errors)


    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=Profiles.objects.get(id=data.get('id'))
            serializer=CreateUpdateProfileSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data']=serializer.data# type: ignore
                return Response(response)
            else :
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status':400,'message':'invalid id'})
        
    def delete(self,request,*args, **kwargs):
        response={'status':200}
        data=request.data 
        try:
            obj=Profiles.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})
    
    
    
######################ADDRESS###########


class AddressDetailView(APIView):
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]
    
    serializer_class = CreateUpdateAddressSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        address_objs=Addresses.objects.all()
        roles=UserDatas.objects.values_list('role', flat=True)
        print(roles)

     
        
        # if i.role=="Player":
        serializer=AddressSerializer(address_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
            # else:
            #     return Response({'status':400,'message':'role is invalid'})
                
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=CreateUpdateAddressSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"Address Added"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=Addresses.objects.get(id=data.get('id'))
            serializer=CreateUpdateAddressSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data']=serializer.data# type: ignore
                return Response(response)
            else :
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status':400,'message':'invalid id'})
        
    def delete(self,request,*args, **kwargs):
        response={'status':200}
        data=request.data 
        try:
            obj=Addresses.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})

    



###########PLAYER##########


class PlayerView(APIView):
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]

    serializer_class = CreateUpdatePlayerSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        player_objs=Players.objects.all()
        serializer=PlayerSerializer(player_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=CreateUpdatePlayerSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"Player Added"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=Players.objects.get(id=data.get('id'))
            serializer=CreateUpdatePlayerSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data']=serializer.data# type: ignore
                return Response(response)
            else :
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status':400,'message':'invalid id'})
        
    def delete(self,request,*args, **kwargs):
        response={'status':200}
        data=request.data 
        try:
            obj=Players.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})

    



###########COACH##########

class CoachView(APIView):
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]

    serializer_class = CreateUpdateCoachSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        coach_objs=Coaches.objects.all()
        serializer=CoachSerializer(coach_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=CreateUpdateCoachSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"Coach Added"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=Coaches.objects.get(id=data.get('id'))
            serializer=CreateUpdateCoachSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data']=serializer.data# type: ignore
                return Response(response)
            else :
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status':400,'message':'invalid id'})
        
    def delete(self,request,*args, **kwargs):
        response={'status':200}
        data=request.data 
        try:
            obj=Coaches.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})

    


########### Ground Provider ##########

class GroundProviderView(APIView):
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]

    serializer_class = CreateUpdateGroundProviderSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        ground_provider_objs=GroundProviders.objects.all()
        serializer=GroundProviderSerializer(ground_provider_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=CreateUpdateGroundProviderSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"Ground Data Added"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=GroundProviders.objects.get(id=data.get('id'))
            serializer=CreateUpdateGroundProviderSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data']=serializer.data# type: ignore
                return Response(response)
            else :
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status':400,'message':'invalid id'})
        
    def delete(self,request,*args, **kwargs):
        response={'status':200}
        data=request.data 
        try:
            obj=GroundProviders.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})

    



###########COURTDETAIl##########

class CourtDetailView(APIView):
    # permission_classes=[IsAuthenticated,]
    # authentication_classes=[JWTAuthentication]

    serializer_class = CreateUpdateCourtDetailSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        court_details_objs=CourtDetails.objects.all()
        serializer=CourtDetailSerializer(court_details_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=CreateUpdateCourtDetailSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"Court Detail Data Added"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=CourtDetails.objects.get(id=data.get('id'))
            serializer=CreateUpdateCourtDetailSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data']=serializer.data# type: ignore
                return Response(response)
            else :
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status':400,'message':'invalid id'})
        
    def delete(self,request,*args, **kwargs):
        response={'status':200}
        data=request.data 
        try:
            obj=CourtDetails.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})
