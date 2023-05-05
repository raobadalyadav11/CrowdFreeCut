from django.urls import path, include
from .views import BookingRequestView
urlpatterns = [
    path('booking-request/<int:id>/', BookingRequestView.as_view(), name="booking_request")
]