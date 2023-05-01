from django.shortcuts import render
from base.views import BaseView
# Create your views here.

class Dashboard(BaseView):
    def get(self, request, *args, **kwargs):
        return render(request, "salon/dashboard.html", {
            
        })