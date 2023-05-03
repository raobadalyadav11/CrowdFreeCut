from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from salon.models import Salon
from account.models import User
from customer.models import BookingRequest

class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request, *args, **kwargs):
        salons =  Salon.objects.all()
        return render(request, self.template_name, {
            'salons': salons,
        })
    
    
class SalonDetailsView(View):
    def get(self, request, *args, **kwargs):
        salon_id = kwargs.get('id')
        salon = Salon.objects.get(id=salon_id)
        queue = BookingRequest.objects.filter(salon=salon, status='Queue').count()
        return render(request, "home/salon.html", {
            'salon': salon,
            'queue_count': queue
        })
    
class LoginSignUpView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("salon:dashboard")
        return render(request, "home/login-signup.html", {
            
        })

    def post(self, request, *args, **kwargs):
        msg = kwargs.get("msg")
        next = request.GET.get("next")
        
        if msg=='signup':
            
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            type = request.POST.get("type")
            password = request.POST.get("password")
            re_password = request.POST.get("re-password")

            if name and email and type and password and re_password and password == re_password and not User.objects.filter(email=email).exists() and type in ("Salon", "Customer", "Admin"):

                user = User()
                user.name = name
                user.email = email
                user.phone = phone
                user.user_type = type
                user.set_password(password)
                user.save()

                user = authenticate(request, email=email, password=password)
                
            else:
                messages.add_message(request, messages.ERROR, "Validation failed!!")
                if next:
                    return redirect(reverse("home:login-signup")+"?next="+next)
                return redirect("home:login-signup")

        elif msg=='login':
            email = request.POST.get("email")
            password = request.POST.get("password")
            print(email, password)

            if email and password:
                user = authenticate(request, email=email, password=password)

                if not user:
                    messages.add_message(request, messages.ERROR, "Kindly check your email or password!!")
                    if next:
                        return redirect(reverse("home:login-signup")+"?next="+next)
                    return redirect("home:login-signup")

            else:
                messages.add_message(request, messages.ERROR, "Validation failed!!")
                if next:
                    return redirect(reverse("home:login-signup")+"?next="+next)
                return redirect("home:login-signup")
        else:
            if next:
                return redirect(reverse("home:login-signup")+"?next="+next)
            return redirect("home:login-signup")

        login(request, user)

        if user.user_type == "Salon":
            return redirect("salon:dashboard")
        
        if user.user_type == "Customer":
            if next:
                return redirect(next)
            return redirect("home:index")
        
        if user.user_type == "Admin":
            pass
