from django.db import models
import uuid

# Create your models here.

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
    reservation_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    move_date = models.DateField()
    origin_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField()
    workers = models.PositiveIntegerField()

    @property
    def total_cost(self):
        return self.service.get_price_per_hour(self.workers) * self.hours

    def __str__(self):
        return f"{self.service.name} - {self.hours}h, {self.workers} workers"

    def __str__(self):
        return f"{self.customer_name} - {self.reservation_number}"

    
