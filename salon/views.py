from django.shortcuts import render
from base.views import BaseView
from django.views import View
# Create your views here.

class Dashboard(BaseView):
    def get(self, request, *args, **kwargs):
        return render(request, "salon/dashboard.html", {

        })
    
class CreateSalonProfile(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "Salon":
            return render(request, "salon/create-salon-profile.html", {
                
            })