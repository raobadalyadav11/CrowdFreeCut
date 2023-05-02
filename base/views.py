from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from salon.models import Salon

class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type=="Salon":
            salon = Salon.objects.filter(user=request.user)
            if not salon:
                return redirect("salon:create-salon-profile")
            
        if not request.user.is_authenticated:
            next = request.GET.get("next")
            if next:
                return redirect(reverse("home:login-signup")+"?next="+next)
            return redirect("home:login-signup")

        elif request.user.user_type == "Salon" and request.path.split("/")[1] != 'salon':
            
            return redirect("salon:dashboard")
        
        elif request.user.user_type == "Admin" and request.path.split("/")[1] != 'superadmin':
            pass
        
        elif request.user.user_type == "Customer" and (request.path.split("/")[1] == 'salon' or request.path.split("/")[1] == 'superadmin'):
            return redirect("home:index")


        return super().dispatch(request, *args, **kwargs)
