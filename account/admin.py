from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group
admin.site.unregister(Group)




class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'name', 'date_joined', 'is_staff', 'is_superuser']
    list_filter = ['is_staff',]
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type',)}),
        ('Personal info', {'fields': ('name', 'phone', 'is_verified')}),
        ('Permissions', {'fields': ('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email', 'user_type', 'customer_type', 'password1', 'password2', 'is_verified', 'is_staff','is_active')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)