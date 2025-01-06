from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()
# Register your models here.

@admin.register(User)
class UserModelAdmin(BaseUserAdmin):
    """
    - The fields to be used in displaying the User model.
    - These override the definitions on the base UserAdmin that reference specific fields on auth.User.
    """
    
    list_display = (
        'id',
        'email',
        'username',
        'name',
        'role',
        'is_active',
    )
    list_filter = ('role', 'is_active')
    fieldsets = (
        ('User Credentials', {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('name', 'username')
        }),
        ('Permissions', {
            'fields': ('role', 'is_active')
        })
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2', 'role')
        }),
    )
    
    search_fields = ('email', 'username')
    ordering = ('email', 'id')
    filter_horizontal = ()

