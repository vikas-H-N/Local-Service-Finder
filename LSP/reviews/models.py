from django.db import models
from django.contrib.auth.models import User
from bookings.models import ServiceRequest

# Create your models here.

class Review(models.Model):
    service_request = models.OneToOneField(
        ServiceRequest,
        on_delete=models.CASCADE,
        related_name="review",
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="written_reviews",
    )

    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.customer.username} - "
            f"{self.rating}/5"
        )
