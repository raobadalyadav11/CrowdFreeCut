from django.db import models
from base.models import BaseModel
from account.models import User



SALON_GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unisex', 'Unisex'),
)


class Salon(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=SALON_GENDER_TYPE)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class SalonService(BaseModel):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="salon/service-image", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.salon.name} - {self.name}"


class SalonImage(BaseModel):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="salon/image")


class SalonReview(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    comment = models.TextField()
    star = models.IntegerField()

    def __str__(self):
        return f"Review by {self.customer.name} for {self.salon.name}"
    

