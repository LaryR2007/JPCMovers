from django.shortcuts import render
from .models import Service, Reservation
from .forms import ReservationForm, ReservationLookupForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def get_quote(request):
    return render(request, 'getquote.html')

def reviews(request):
    return render(request, 'reviews.html')

def reservation_success(request, reservation_number):
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)
    total = reservation.total_cost()
    return render(request, 'reservation_success.html', {'reservation': reservation, 'total': total})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            total = reservation.total_cost()
#----------------Email subject and message-------------------
            context = {
                'reservation': reservation,
                'total': total
            }

            # Render HTML email content
            html_content = render_to_string("moving/reservation_email.html", context)
            text_content = strip_tags(html_content)  # fallback for email clients that don't support HTML

            subject = f"Reservation Confirmation - JPC Best Movers"
            from_email = 'JPC Best Movers <jpcbestmovers@gmail.com>'
            to = [reservation.customer_email]
            cc = ['jpcbestmovers@gmail.com']  # Send yourself a copy

            msg = EmailMultiAlternatives(subject, text_content, from_email, to, cc=cc)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
#---------------------------DONE-------------------------
            return redirect('reservation_success', reservation_number=reservation.reservation_number)
    else:
        form = ReservationForm()
    return render(request, 'make_reservation.html', {'form': form})

def lookup_reservation(request):
    if request.method == 'POST':
        form = ReservationLookupForm(request.POST)
        if form.is_valid():
            res_num = form.cleaned_data['reservation_number']
            try:
                reservation = Reservation.objects.get(reservation_number=res_num)
                return redirect('edit_reservation', reservation_number=res_num)
            except Reservation.DoesNotExist:
                form.add_error('reservation_number', 'Reservation not found.')
    else:
        form = ReservationLookupForm()
    return render(request, 'lookup_reservation.html', {'form': form})

def edit_reservation(request, reservation_number):
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return render(request, 'reservation_success.html', {'reservation': reservation})
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form, 'reservation': reservation})