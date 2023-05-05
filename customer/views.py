from django.shortcuts import render, redirect
from django.views import View
from base.views import BaseView
from .models import BookingRequest
from salon.models import Salon
from datetime import datetime
from django.contrib import messages

class BookingRequestView(BaseView):
     def post(self, request, *args, **kwargs):
        try:
            salon_id = kwargs.get('id')
            salon = Salon.objects.get(id=salon_id)
            services = request.POST.getlist("services")
            special_req = request.POST.get("spec-req")
            book_req = BookingRequest()
            book_req.customer = request.user
            book_req.salon = salon
            book_req.booking_datetime = datetime.now()
            book_req.message = special_req
            book_req.service = ",".join(services)    
            book_req.save()
            messages.add_message(request, messages.SUCCESS, "Booking Successful!!")
        except Exception as e:
            messages.add_message(request, messages.ERROR, "Somthing went wrong!!")
        return redirect('home:salon', salon_id)