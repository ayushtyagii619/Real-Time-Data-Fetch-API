from django.contrib import admin
from .models import AyushUser
from django.contrib.auth.admin import UserAdmin

class AyushAdmin(UserAdmin):
    list_display = ('id','email','name','tc','is_superuser','is_admin','is_staff')
    list_filter = ('is_admin',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'tc')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'tc', 'password1', 'password2'),
        }),
    )
    search_fields  = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

admin.site.register(AyushUser,AyushAdmin) 