from django.contrib import admin
from sabpaisa_app.models import NewUser
from django.contrib.auth.admin import UserAdmin

class AyushAdmin(UserAdmin):
    list_display = ('id','email','name','tc','is_admin','is_staff','is_superuser')
    list_filter = ('is_admin','is_staff','is_superuser')
    fieldsets = (
        ('User Credentials',{'fields':('email','password')}),
        ('Personal info',{'fields':('name','tc')}),
        ('Permissions',{'fields':('is_admin','is_staff','is_superuser')}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','name','tc','password1','password2'),
        }),

    )
    search_fields  = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

admin.site.register(NewUser,AyushAdmin) 