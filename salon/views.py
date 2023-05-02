from django.shortcuts import render, redirect
from base.views import BaseView
from django.views import View
from salon.models import Salon
from django.contrib.auth import logout
# Create your views here.

class Dashboard(BaseView):
    def get(self, request, *args, **kwargs):
        return render(request, "salon/dashboard.html", {

        })


class DashboardFunctionView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            msg = kwargs.get("msg")

            if msg == "request":
                req = True if request.POST.get("request") == "on" else False
                salon = Salon.objects.get(user__id=request.user.id)
                salon.is_open = req
                salon.save()

            if msg == "logout":
                logout(request)
        return redirect("salon:dashboard")
    
class CreateSalonProfile(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "Salon":
            return render(request, "salon/create-salon-profile.html", {

            })
        
    def post(self, request, *args, **kwargs):
        name = request.POST.get("salon-name")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        location = request.POST.get("location")
        address = request.POST.get("address")
        description = request.POST.get("description")

        salon = Salon()
        salon.name = name
        salon.gender = gender
        salon.phone = phone
        salon.address = address
        salon.description = description
        salon.location = location
        salon.user = request.user
        salon.save()
        return redirect("salon:dashboard")