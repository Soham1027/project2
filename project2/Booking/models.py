from django.db import models
from django.utils import timezone
from enum import Enum
from django.db.models import Case, Value, When, CharField
from django.core.validators import MaxValueValidator
from SportingBuddiesApp.models import(
    Players,
    Coaches,
    GroundProviders,
    Profiles
)
PROFILES = (
    ("Player", "Player"),
    ("Coach", "Coach"),
    
   
  
)
# Create your models here.

class Bookings(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Profiles,on_delete=models.CASCADE,blank=True, null=True)
    player_data_ids=models.ForeignKey(Players,related_name="player_id",on_delete=models.CASCADE)
    player_1=models.ForeignKey(Players,related_name="player_1",on_delete=models.CASCADE)
    player_2=models.ForeignKey(Players,related_name="player_2",on_delete=models.CASCADE,null=True, blank=True, db_constraint=False)
    player_3=models.ForeignKey(Players,related_name="player_3",on_delete=models.CASCADE,null=True, blank=True, db_constraint=False)
    coach_data_ids=models.ForeignKey(Coaches,on_delete=models.CASCADE,null=True, blank=True, db_constraint=False)
    ground_provider_ids=models.ForeignKey(GroundProviders,on_delete=models.CASCADE,null=True, blank=True, db_constraint=False)
    coach_payment=models.PositiveSmallIntegerField()
    court_payment=models.PositiveSmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)
    confirm_status=models.BooleanField(default=True)
    

    def __str__(self) -> str:
      
        return str(self.id)
   
    
    

class PaymentDatas(models.Model):
    id=models.AutoField(primary_key=True)
    booking_id=models.ForeignKey(Bookings,on_delete=models.CASCADE)
    coach_refund=models.PositiveSmallIntegerField()
    court_refund=models.PositiveSmallIntegerField()
    
    reason=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)
    cancellation_time=models.DateTimeField(blank=True, null=True)
    cancel_status=models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        if self.cancel_status:
            self.cancellation_time=timezone.now()
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
      
        return str(self.id)
    
    
class ProfileType(Enum):
    PLAYER='player'
    COACH='coach'
class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.FloatField(validators=[MaxValueValidator(10.0)],null=True)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    players_data_id = models.ForeignKey(Players, on_delete=models.CASCADE, null=True)
    coach_data_id = models.ForeignKey(Coaches, on_delete=models.CASCADE, null=True)
    review_from=models.CharField(max_length=10,choices=[(choice.name,choice.value) for choice in ProfileType]) 
   
   
    def __str__(self) -> str:
      
        return str(self.id)
   
    

