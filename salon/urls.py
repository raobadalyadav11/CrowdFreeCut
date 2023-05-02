from django.urls import path
from salon.views import Dashboard, CreateSalonProfile, DashboardFunctionView

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('dashboard/<str:msg>/', Dashboard.as_view(), name='current-card-function'),
    path("dashboard-function/<str:msg>/", DashboardFunctionView.as_view(), name="dashboard-post"),
    path("create-salon-profile/", CreateSalonProfile.as_view(), name="create-salon-profile"),
]