from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter


from Booking.views import (
    BookingView,
    ReviewDataView,
    PaymentDataView
)
from DataAvailability.views import(
    ProfileAvailabilityView,
    CourtAvailabilityView,
)


from .views import (
    # GetPlayerView,
    # PostPlayerView,
 
    PlayerView,
    CoachView,
    GroundProviderView,
  
   
    CourtDetailView,
    TestProfileDetailView,
    UserView,
    ProfileDetailView,
    LogoutView,
    LoginView,
    AddressDetailView,
    ProfileRetrieveUpdateDestroyAPIView,
    TestToken,



    
)

urlpatterns = [
 
  
  
    # path('player/',PlayerView.as_view(),name="player"),
    # path('coach/',CoachView.as_view(),name="coach"),
    path('ground_provider/',GroundProviderView.as_view(),name="ground_provider"),
  
    path('profile_availability/',ProfileAvailabilityView.as_view(),name="profile_availability"),
    path('court_availability/',CourtAvailabilityView.as_view(),name="court_availability"),
  
    
    path('register/',UserView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
   
    # path('profile_detail/',ProfileDetailView.as_view(),name="profile"),
    path('court_detail/',CourtDetailView.as_view(),name="court_detail"),
    
   
    
    path('profile/',TestProfileDetailView.as_view(),name="profile"),
   
    path('profile/<int:pk>/',ProfileRetrieveUpdateDestroyAPIView.as_view(),name="profile"),
    
    path('data/',TestToken.as_view(),name="data_test"),

    path('booking/',BookingView.as_view(),name="booking"),
    path('review/',ReviewDataView.as_view(),name="review"),
    path('payment/',PaymentDataView.as_view(),name="payment"),
]