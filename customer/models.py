from django.db import models
from base.models import BaseModel
from account.models import User
from salon.models import Salon

BOOKING_STATUS = (
    ('Queue', 'Queue'),
    ('On Hold', 'On Hold'),
    ('Completed', 'Completed'),
    ('Cancel', 'Cancel')
)

NOTIFICATION_TYPE = (
    ('Danger', 'danger'),
    ('Warning', 'warning'),
    ('Info', 'info'),
    ('Success', 'success'),
)  

class BookingRequest(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=BOOKING_STATUS, default='Queue')
    booking_datetime = models.DateTimeField()
    service = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)
    token_no = models.CharField(max_length=100, null=True, blank=True)
    completion_time = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Booking request at {self.booking_datetime}"
  

class CustomerNotification(BaseModel):
    title = models.CharField(max_length=200)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_request = models.ForeignKey(BookingRequest, on_delete=models.SET_NULL, null=True)
    notify_datetime = models.DateTimeField()
    short_desc = models.TextField()
    type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE)

    def __str__(self):
        return f"{self.title} - {self.customer.name}" if self.customer else self.title
     
    