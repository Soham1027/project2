from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Booking.views import (
    BookingView,
    ReviewDataView,
    PaymentDataView
)
from DataAvailability.views import (
    ProfileAvailabilityView,
    CourtAvailabilityView,
)

from .views import (


    
   
    ProfileDetailView,

    CourtDetailView,
    TestProfileDetailView,
    UserView,

    LogoutView,
    LoginView,

    TestProfileRetrieveUpdateDestroyAPIView,
    
    ProfileRetrieveUpdateDestroyAPIView
   

)

urlpatterns = [


    # path('ground_provider/', GroundProviderView.as_view(), name="ground_provider"),
    # path('ground_provider/<int:pk>/', GroundProviderUpdateDestroyAPIView.as_view(), name="ground_provider"),

    path('profile_availability/', ProfileAvailabilityView.as_view(), name="profile_availability"),
    path('court_availability/', CourtAvailabilityView.as_view(), name="court_availability"),

    path('register/', UserView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),


    path('court_detail/', CourtDetailView.as_view(), name="court_detail"),

    path('profile/', TestProfileDetailView.as_view(), name="profile"),

    path('ground_profile/', ProfileDetailView.as_view(), name="ground_profile"),

    path('ground_profile/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name="ground_profile"),
    
    path('profile/<int:pk>/', TestProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile"),

 
    path('booking/', BookingView.as_view(), name="booking"),
    path('review/', ReviewDataView.as_view(), name="review"),
    path('payment/', PaymentDataView.as_view(), name="payment"),
]
