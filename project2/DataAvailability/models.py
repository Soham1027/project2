from django.db import models
from SportingBuddiesApp.models import(
    Profiles,
    CourtDetails
    
)
# Create your models here.



class DataTimes(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(auto_now=False, auto_now_add=False)
    start_time=models.TimeField(auto_now=False, auto_now_add=False)
    end_time=models.TimeField(auto_now=False, auto_now_add=False)
   
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models. DateTimeField(auto_now=True)

class ProfileAvailabilities(DataTimes):
  

    profiles_ids=models.ForeignKey(Profiles,on_delete=models.CASCADE)

    
    def __str__(self) -> str:
      
        return str(self.id) #type:ignore

class CourtAvailabilities(DataTimes):
 
    courts_ids=models.ForeignKey(CourtDetails,on_delete=models.CASCADE)

    
    def __str__(self) -> str:
      
        return  str(self.id)   #type:ignore
    
