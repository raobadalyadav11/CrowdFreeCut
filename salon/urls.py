from django.urls import path
from salon.views import Dashboard

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]