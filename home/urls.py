from django.urls import path
from home.views import HomeView, SalonDetailsView, LoginSignUpView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('salon/<int:id>', SalonDetailsView.as_view(), name="salon"),
    path('login-signup/', LoginSignUpView.as_view(), name="login-signup"),
    path("login-signup/post/<str:msg>/", LoginSignUpView.as_view(), name="login-signup-post"),
]