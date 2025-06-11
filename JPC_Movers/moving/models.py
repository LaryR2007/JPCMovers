from django.db import models
import uuid
from decimal import Decimal
from django.utils import timezone

# Create your models here.
def generate_reservation_number():
        return uuid.uuid4().hex[:8].upper()  
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # Only store base price (for 1 worker per hour)
    base_price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

    def get_price_per_hour(self, worker_count):
        if worker_count >= 1:
            return self.base_price_per_hour * worker_count
        raise ValueError("Worker count must be at least 1")

    def __str__(self):
        return self.name

class Reservation(models.Model):  
    reservation_number = models.CharField(
        max_length=8,
        unique=True,
        default= generate_reservation_number,
        editable=False
    )
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    move_datetime = models.DateTimeField()
    origin_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    workers = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])
    hours = models.IntegerField(choices=[(i, str(i)) for i in range(1, 13)])
     

    def total_cost(self):
        return self.service.base_price_per_hour * Decimal(self.workers) * Decimal(self.hours)

    def __str__(self):
        return f"Reservation {self.reservation_number} for {self.customer_name}"

    
