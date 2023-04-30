from django.urls import path
from home.views import HomeView, SaloonDetailsView, LoginSignUpView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('saloon/', SaloonDetailsView.as_view(), name="saloon"),
    path('login-signup/', LoginSignUpView.as_view(), name="login-signup"),
]