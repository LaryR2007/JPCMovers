from django.db import models
import uuid

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # Prices based on number of workers
    price_per_hour_1_worker = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_hour_2_workers = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_hour_3_workers = models.DecimalField(max_digits=6, decimal_places=2)

    def get_price_per_hour(self, worker_count):
        if worker_count == 1:
            return self.price_per_hour_1_worker
        elif worker_count == 2:
            return self.price_per_hour_2_workers
        elif worker_count == 3:
            return self.price_per_hour_3_workers
        else:
            raise ValueError("Unsupported worker count")

    def __str__(self):
        return self.name

    
class Reservation(models.Model):
    reservation_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    move_date = models.DateField()
    origin_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)
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

    
