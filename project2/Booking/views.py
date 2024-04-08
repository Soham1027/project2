from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import (
    CreateUpdateBookingSerializer,
    CreateUpdatePaymentDataSerializer,
    CreateUpdateReviewSerializer,
    BookingSerializer,
    ReviewSerializer,
    PaymentDataSerializer
)

from .models import (
    Bookings,
    PaymentDatas,
    Reviews
)
# Create your views here.

########### Payment view ############
class PaymentDataView(APIView):

    serializer_class = CreateUpdatePaymentDataSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        booking_objs=PaymentDatas.objects.all()
        serializer=PaymentDataSerializer(booking_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=CreateUpdatePaymentDataSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"Booking Cancel"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=PaymentDatas.objects.get(id=data.get('id'))
            serializer=CreateUpdatePaymentDataSerializer(obj,data=data,partial=True)
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
            obj=PaymentDatas.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})




########### Review ############
class ReviewDataView(APIView):

    serializer_class = CreateUpdateReviewSerializer
    
    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        reviews_objs = Reviews.objects.all().filter(review_from="player")
        serializer = ReviewSerializer(reviews_objs, many=True)
        response['data'] = serializer.data   #type:ignore
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CreateUpdateReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Review Added"}
            return Response(response)
        return Response(serializer.errors)
    
    def patch(self, request, *args, **kwargs):
        response = {'status': 200}
        data = request.data
        try:
            obj = Reviews.objects.get(id=data.get('id'))
            serializer = CreateUpdateReviewSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data  #type:ignore
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
            obj = Reviews.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status': 200, 'message': "Deleted"})
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': "Invalid id"})


########### BOOKING ############
class BookingView(APIView):

    serializer_class = CreateUpdateBookingSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        booking_objs=Bookings.objects.all()
        serializer=BookingSerializer(booking_objs,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=CreateUpdateBookingSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"BookingData Added"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=Bookings.objects.get(id=data.get('id'))
            serializer=CreateUpdateBookingSerializer(obj,data=data,partial=True)
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
            obj=Bookings.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})
