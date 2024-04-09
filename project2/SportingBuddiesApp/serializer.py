from django.http import JsonResponse
from rest_framework import serializers
from phonenumber_field.modelfields import PhoneNumberField #type:ignore
from phonenumber_field.phonenumber import to_python  #type:ignore


from django.contrib.auth.hashers import make_password
from .models import(
    UserDatas,
    Players,
    Coaches,
    CourtDetails,
    Profiles,
    Addresses,
    GroundProviders,
   

)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True, style={'input_type': 'password', 'placeholder': 'Password'})
    confirm_password=serializers.CharField(write_only=True,required=True, style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = UserDatas
        fields = ('id','email', 'password','role','confirm_password')
        
        
    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        validated_data['confirm_password']=make_password(validated_data['confirm_password'])
        return super().create(validated_data)
     
    def validate(self, attrs):
        if attrs['confirm_password'] != attrs['password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True, style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = UserDatas
        fields = ('id','email', 'password','role')
        
        
   

class ProfileSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(region="IN") # type: ignore
    # user_data_id=UserSerializer(many=False)
 
  

    # user_data_id= serializers.StringRelatedField(many=False)
    class Meta:
        model=Profiles
        fields=('id','name','birthdate','gender','profile_pic','nationality','phone','user_data_id')
        
    def validate_phone(self,value):
        phone_number=to_python(value)
        if phone_number:
            if not phone_number.is_valid():
                raise serializers.ValidationError("Enter valid phone number")
            if not str(phone_number.country_code)=="91":
                raise serializers.ValidationError("Number has must extension +91")
        return value

  
class CreateUpdateProfileSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(region="IND") # type: ignore
   
    class Meta:
        model=Profiles
        fields=('id','name','birthdate','gender','profile_pic','nationality','phone','user_data_id')
        

class AddressSerializer(serializers.ModelSerializer):
    
    zip_code=serializers.IntegerField()
   
   
    # profile_data_id=ProfileSerializer(many=False)
    class Meta:
        model=Addresses
        # fields=('id','flat_no','landmark','area','city','zip_code')
        fields=('id','flat_no','landmark','area','zip_code')
        
    def validate_zip_code(self,value):
        
       
        if not 2<len(str(value))<7:
            raise serializers.ValidationError("Enter valid Zip code")
        
        return value

  
class CreateUpdateAddressSerializer(serializers.ModelSerializer):
    zip_code =serializers.IntegerField()
    
    class Meta:
        model=Addresses
        # fields=('id','flat_no','landmark','area','city','zip_code')
        fields=('id','flat_no','landmark','area','zip_code')
        
    def validate_zip_code(self,value):
        
       
        if not 2<len(str(value))<7:
            raise serializers.ValidationError("Enter valid Zip code")
        
        return value
    


       
class PlayerSerializer(serializers.ModelSerializer):
    player_profile_id=ProfileSerializer(many=False)
    # player_profile_id= serializers.StringRelatedField(many=False)
    
    class Meta:
        model=Players
        fields=('id','aita_ranking','skills','player_profile_id')
        
class CreateUpdatePlayerSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Players
        fields=('id','aita_ranking','skills','player_profile_id')
        
     
            
        
class CoachSerializer(serializers.ModelSerializer):
    coaches_profile_id=ProfileSerializer(many=False)
    # coaches_profile_id= serializers.StringRelatedField(many=False)
   
    class Meta:
        model=Coaches
        fields=('id','qualification','certificate','prices','technique','specialities','experience','coaches_profile_id')

class CreateUpdateCoachSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Coaches
        fields=('id','qualification','certificate','prices','technique','specialities','experience','coaches_profile_id')

 
class GroundProviderSerializer(serializers.ModelSerializer):
    ground_provider_profile_id=ProfileSerializer(many=False)
    # ground_provider_profile_id= serializers.StringRelatedField(many=False)
    
    class Meta:
        model=GroundProviders
        fields=('id','ground_name','ammenities','facilities','ground_provider_profile_id')

class CreateUpdateGroundProviderSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=GroundProviders
        fields=('id','ground_name','ammenities','facilities','ground_provider_profile_id')

 
 
 
 
        
class CourtDetailSerializer(serializers.ModelSerializer):
    ground_datas_ids=GroundProviderSerializer(many=False)
    # ground_datas_ids= serializers.StringRelatedField(many=False)
    
    class Meta:
        model=CourtDetails
        fields=('id','court_name','surface_type','price','light_availability','ground_datas_ids')

        
class CreateUpdateCourtDetailSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=CourtDetails
        fields=('id','court_name','surface_type','price','light_availability','ground_datas_ids')

 
        

class UserLogoutSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = UserDatas
        fields = ['email']
        
        
        
        

       
class TestAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ('flat_no','landmark','area','city','zip_code')
class TestPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        
        
        fields =('aita_ranking','skills')
        
    def create(self, validated_data):
     
        player_data = None
     
        user_data_id=validated_data.get('player_profile_id').user_data_id
        role=user_data_id.role
        print("jkl;kl",role)
        # if role=='Player':
        #     player_data=validated_data.pop('player',None)
        # elif role=='Coach':
        #     coach_data=validated_data.pop('coach',None)
        
       
    
class TestCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaches
        fields =('qualification','certificate','prices','technique','specialities','experience')

class TestProfileSerializer(serializers.ModelSerializer):
    addresses = TestAddressSerializer(required=False)
    player=TestPlayerSerializer(required=False)
    coach=TestCoachSerializer(required=False)
    
    

    class Meta:
        model = Profiles
        fields = ('id','name','birthdate','gender','nationality','phone','profile_pic','user_data_id','addresses','player','coach')

  
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        user_data_id=instance.user_data_id
        
        if user_data_id.role=='Player':
            representation.pop('coach',None)
        elif user_data_id.role=='Coach':
            representation.pop('player',None)
        
        return {"profiles":representation}
    
    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', None)
        player_data = validated_data.pop('player', None)
        coach_data=validated_data.pop('coach',None)
        profile_instance = Profiles.objects.create(**validated_data)
        if addresses_data:
            Addresses.objects.create(profile_data_id=profile_instance, **addresses_data)
        if player_data:
            Players.objects.create(player_profile_id=profile_instance, **player_data)
        if coach_data:
            Coaches.objects.create(coaches_profile_id=profile_instance, **coach_data)
       
       
        return profile_instance

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('addresses', None)
        player_data=validated_data.pop('player',None)
        coach_data=validated_data.pop('coach',None)
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.user_data_id = validated_data.get('user_data_id', instance.user_data_id)
        instance.save()

        if addresses_data:
            if instance.addresses:
                addresses_serializer = TestAddressSerializer(instance.addresses, data=addresses_data)
                if addresses_serializer.is_valid():
                    addresses_serializer.save()
            else:
                Addresses.objects.create(profile_data_id=instance, **addresses_data)
                
        if player_data:
            if instance.player:
                player_serializer = TestPlayerSerializer(instance.player, data=player_data)
                if player_serializer.is_valid():
                    player_serializer.save()
            else:
                Players.objects.create(player_profile_id=instance, **player_data)
        
        if coach_data:
            if instance.coach:
                coach_serializer = TestCoachSerializer(instance.coach, data=coach_data)
                if coach_serializer.is_valid():
                    coach_serializer.save()
            else:
                Coaches.objects.create(coaches_profile_id=instance, **coach_data)
                
                
       
        return (instance)
  