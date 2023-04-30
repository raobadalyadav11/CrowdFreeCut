from django.shortcuts import render
from django.views import View

class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class SaloonDetailsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/saloon.html", {

        })
    
class LoginSignUpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/login-signup.html", {
            
        })