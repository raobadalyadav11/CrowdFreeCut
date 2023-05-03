from django.contrib import admin
from salon.models import Salon, SalonService, SalonReview, SalonImage

# Register your models here.
admin.site.register([SalonImage, SalonReview, SalonService])

class SalonServiceInline(admin.TabularInline):
    model = SalonService

@admin.register(Salon)
class SalonModelAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    inlines = [
        SalonServiceInline
    ]