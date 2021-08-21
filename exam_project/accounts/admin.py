from django.contrib import admin

from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_number']
    fields = ['phone_number', 'user']
    readonly_fields = ['id']


# Register your models here.
