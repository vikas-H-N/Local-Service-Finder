from django.db import models
from django.contrib.auth.models import User
from services.models import Service

# Create your models here.


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="service_requests",
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="requests",
    )

    description = models.TextField(
        help_text="Describe the service you need."
    )

    service_address = models.TextField()

    preferred_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Request #{self.pk} - "
            f"{self.customer.username} - {self.service.title}"
        )
