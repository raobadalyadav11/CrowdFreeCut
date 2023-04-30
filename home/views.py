from django.shortcuts import render
from django.views import View
from salon.models import Salon

class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request, *args, **kwargs):
        salons =  Salon.objects.all()
        return render(request, self.template_name)
    
    
class SaloonDetailsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/saloon.html", {

        })
    
class LoginSignUpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/login-signup.html", {
            
        })
