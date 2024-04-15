
from django.utils import timezone
from typing import Any
from django.db import models
from django.core.validators import EmailValidator,MinLengthValidator,MaxValueValidator
from django.contrib.auth.models import AbstractUser
from indian_cities.dj_city import cities    #type:ignore
from django_countries.fields import CountryField    #type:ignore
from phonenumber_field.modelfields import PhoneNumberField  #type:ignore
# Create your models here.

SKILLS_CHOICES = (
    ("RECREATION", "RECREATION"),
    ("BASIC", "BASIC"),
    ("INTERMEDIATE", "INTERMEDIATE"),
    ("EXPERT", "EXPERT")
  
)

ROLE_CHOICES = (
    ("Player", "Player"),
    ("Coach", "Coach"),
    ("Ground Owner", "Ground Owner")
   
  
)


GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHERS", "OTHERS")
   
  
)

SURFACE_CHOICES = (
    ("Sandy Soil", "Sandy Soil"),
    ("Silt Soil", "Silt Soil"),
    ("Clay Soil", "Clay Soil")
   
  
)
    

class UserDatas(models.Model):
    id=models.AutoField(primary_key=True)	
    email=models.EmailField(max_length=50,validators=[EmailValidator(message="enter valid email")])
    password=models.CharField(max_length=300,validators=[MinLengthValidator(4)])
    confirm_password=models.CharField(max_length=300)
    role=models.CharField(choices=ROLE_CHOICES,max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email
    
   

   


class Profiles(models.Model):
    id=models.AutoField(primary_key=True)	
    name=models.CharField(max_length=50)
    birthdate=models.DateField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=10)
    nationality = models.CharField(max_length=200, choices=list(CountryField().choices) + [('', 'Select Country')])
    phone=PhoneNumberField()
    profile_pic=models.ImageField(upload_to='static/upload_images/', null=True,blank=True)
    user_data_id=models.OneToOneField(UserDatas,on_delete=models.CASCADE,blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   	
    def __str__(self) -> str:
        return self.user_data_id.role #type:ignore

    

class Addresses(models.Model):
    id=models.AutoField(primary_key=True)	
    flat_no=models.CharField(max_length=5)
    landmark=models.TextField()
    area=models.TextField() 
   
    city = models.CharField(choices=cities, max_length=20,blank=True, null=True)
    zip_code=models.IntegerField()
   
    profile_data_id=models.OneToOneField(Profiles,on_delete=models.CASCADE,null=True,related_name="addresses")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)
   	
    def __str__(self) -> str:
        print(self.profile_data_id)
        return str(self.id) # type: ignore
    
  
 

class Players(models.Model):
    id=models.AutoField(primary_key=True)
  
    aita_ranking=models.IntegerField(blank=True, null=True)
 
    skills=models.CharField(max_length=20,choices=SKILLS_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)
    player_profile_id=models.OneToOneField(Profiles,on_delete=models.CASCADE,null=True,related_name="player")
   	
    def __str__(self) -> str:
        return (self.player_profile_id.user_data_id.role) #type:ignore
    
class Coaches(models.Model):
    id=models.AutoField(primary_key=True)
    qualification=models.CharField(max_length=50)
    certificate=models.TextField(blank=True, null=True)
    prices=models.IntegerField()
    technique=models.CharField(max_length=50)
    specialities=models.CharField(choices=SKILLS_CHOICES,null=True,max_length=15)
    experience=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)
    coaches_profile_id=models.OneToOneField(Profiles,on_delete=models.CASCADE,null=True,related_name="coach")
   	

    def __str__(self) -> str:
        return self.coaches_profile_id.name #type:ignore

 

class GroundProviders(models.Model):
    id=models.AutoField(primary_key=True)
    ground_name=models.CharField(max_length=50)
    ammenities=models.TextField()
    facilities=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)
    ground_provider_profile_id=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
   	


    
    def __str__(self) -> str:
        return self.ground_name#type:ignore
 


    
class CourtDetails(models.Model):
    id=models.AutoField(primary_key=True)
    court_name=models.CharField(max_length=50)
    surface_type=models.CharField(max_length=20,choices=SURFACE_CHOICES)
    price=models.IntegerField()
    light_availability=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)

    ground_datas_ids=models.ForeignKey(GroundProviders,on_delete=models.CASCADE,null=True)

    
    def __str__(self) -> str:
        # print(self.ground_datas_ids.ground_provider_profile_id.user_data.id.role)
        return self.court_name





