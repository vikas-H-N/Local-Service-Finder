from django.contrib import admin
from .models import ServiceRequest

# Register your models here.

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "service",
        "status",
        "created_at",
    )

    list_filter = ("status", "created_at")
    search_fields = (
        "customer__username",
        "service__title",
    )