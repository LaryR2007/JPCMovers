from django.contrib import admin
from .models import Service, Reservation


admin.site.register(Service)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email','customer_phone', 'move_datetime', 'is_canceled', 'created_at')
    list_filter = ('move_datetime', 'is_canceled')
    search_fields = ('customer_name', 'customer_email', 'customer_phone', 'reservation_number')
    actions = ['cancel_reservations']

    def cancel_reservations(self, request, queryset):
        queryset.update(is_canceled=True)
    cancel_reservations.short_description = "Cancel selected reservations"
# Register your models here.

