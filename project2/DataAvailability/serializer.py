from rest_framework import serializers


from django.contrib.auth.hashers import make_password
from .models import(
    ProfileAvailabilities,
    CourtAvailabilities,
    
)
from SportingBuddiesApp.serializer import(
    ProfileSerializer,
    CourtDetailSerializer
)

        
class ProfileAvailabilitySerializer(serializers.ModelSerializer):
    profiles_ids=ProfileSerializer(many=False)
    # profiles_ids= serializers.StringRelatedField(many=False)
    
    class Meta:
        model=ProfileAvailabilities
        fields=('id','date','start_time','end_time','profiles_ids')


        
class CreateUpdateProfileAvailabilitySerializer(serializers.ModelSerializer):
  
    class Meta:
        model=ProfileAvailabilities
        fields=('id','date','start_time','end_time','profiles_ids')

 
class CourtAvailabilitySerializer(serializers.ModelSerializer):
    # courts_ids=CourtDetailSerializer(many=False)
    courts_ids= serializers.StringRelatedField(many=False)
    
    class Meta:
        model=CourtAvailabilities
        fields=('id','date','start_time','end_time','courts_ids')


        
class CreateUpdateCourtAvailabilitySerializer(serializers.ModelSerializer):
  
    class Meta:
        model=CourtAvailabilities
        fields=('id','date','start_time','end_time','courts_ids')
