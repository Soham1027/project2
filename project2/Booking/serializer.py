from rest_framework import serializers
from phonenumber_field.modelfields import PhoneNumberField #type:ignore
from phonenumber_field.phonenumber import to_python  #type:ignore


from django.contrib.auth.hashers import make_password
from .models import(
    Bookings,
    PaymentDatas,
    Reviews
)
from SportingBuddiesApp.serializer import(
    PlayerSerializer,
    CoachSerializer
)

 
class BookingSerializer(serializers.ModelSerializer):
    # player_data_ids=PlayerSerializer(many=False)
    player_data_ids= serializers.StringRelatedField(many=False)
    player_1=serializers.StringRelatedField(many=False)
    # coach_data_ids=CoachSerializer(many=False)
    coach_data_ids= serializers.StringRelatedField(many=False)
    
    # ground_provider_ids=GroundProviderSerializer(many=False)
    ground_provider_ids= serializers.StringRelatedField(many=False)
    
    class Meta:
        model=Bookings
        fields= ('id','player_data_ids','player_1','player_2','player_3','coach_data_ids','ground_provider_ids','coach_payment','court_payment','confirm_status')
       
    

class CreateUpdateBookingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Bookings
        fields= ('id','player_data_ids','player_1','player_2','player_3','coach_data_ids','ground_provider_ids','coach_payment','court_payment','confirm_status')



class PaymentDataSerializer(serializers.ModelSerializer):
    # booking_id=BookingSerializer(many=False)
    booking_id= serializers.StringRelatedField(many=False)
    
    class Meta:
        model=PaymentDatas
        fields=('id','coach_refund','court_refund','reason','cancel_status','booking_id')

class CreateUpdatePaymentDataSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=PaymentDatas
        fields=('id','coach_refund','court_refund','reason','cancel_status','booking_id')
 
       
class ReviewSerializer(serializers.ModelSerializer):
    players_data_id = serializers.StringRelatedField(many=False)
    coach_data_id = serializers.StringRelatedField(many=False)
    # review_from = serializers.SerializerMethodField()
    # review_to = serializers.SerializerMethodField()

    class Meta:
        model = Reviews
        fields = ('id', 'rating', 'review', 'players_data_id', 'coach_data_id','review_from')


    # def get_review_from(self, obj):
    #     return "Coach" if obj.coach_to_player else "Player"

    # def get_review_to(self, obj):
    #     return "Player" if obj.coach_to_player else "Coach"

        
class CreateUpdateReviewSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Reviews
        fields = ('id', 'rating', 'review', 'players_data_id', 'coach_data_id','review_from')
        

