from django.contrib import admin
from salon.models import Salon, SalonService, SalonReview, SalonImage

# Register your models here.
admin.site.register([SalonImage, SalonReview, Salon, SalonService])