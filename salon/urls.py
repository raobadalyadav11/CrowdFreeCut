from django.urls import path
from salon.views import Dashboard, CreateSalonProfile

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path("create-salon-profile/", CreateSalonProfile.as_view(), name="create-salon-profile"),
]