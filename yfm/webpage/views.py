from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import PageSection, TimeSlot, Booking
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class HomeListView(ListView):
    model = PageSection
    template_name = 'webpage/base.html'




def calendar_view(request):
    return render(request, "calendar.html")

def times_view(request, day):
    times = TimeSlot.objects.filter(date=day, is_booked=False).order_by("time")
    return render(request, "times.html", {"times": times, "day": day})

def book_view(request, slot_id):
    slot = get_object_or_404(TimeSlot, id=slot_id, is_booked=False)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        Booking.objects.create(slot=slot, name=name, email=email)
        slot.is_booked = True
        slot.save()

        return redirect("success") # gotowa rezerwacja

    return render(request, "book.html", {"slot": slot}) #form - rezerwuj


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('imie') or request.POST.get('name') or 'Anonim'
        email = request.POST.get('email')
        message = request.POST.get('wiadomosc') or request.POST.get('message') or ''

        subject = f'Kontakt ze strony: {name}'
        body = message + "\n\n" + f'Od: {name} <{email}>'

        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'pawel.sierz@gmail.com')
        recipient = [email] #[getattr(settings, 'CONTACT_EMAIL', from_email)]

        send_error = None
        try:
            send_mail(subject, body, from_email, recipient, fail_silently=False)
        except Exception as e:
            send_error = str(e)


    if request.method == 'POST':
        name = request.POST.get('imie') or request.POST.get('name') or 'Anonim'
        email = request.POST.get('email')
        message = request.POST.get('wiadomosc') or request.POST.get('message') or ''

        subject = f'Kontakt ze strony: {name}'
        body = message + "\n\n" + f'Od: {name} <{email}>'

        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'pawel.sierz@gmail.com')
        recipient = [email]

        try:
            send_mail(subject, body, from_email, recipient, fail_silently=False)
        except Exception:
            # ignore send errors here; user requested always redirect to main
            pass

    # Always redirect user to the main page regardless of POST result
    return redirect('base')

@require_POST
@csrf_protect
def booking(request):
    """Obsługuje przesłanie formularza rezerwacji"""
    try:
        # Pobierz dane z formularza
        data_od = request.POST.get('data_od')
        data_do = request.POST.get('data_do')
        godzina_od = request.POST.get('godzina_od')
        godzina_do = request.POST.get('godzina_do')
        imie_naz = request.POST.get('imie_naz')
        spos_kontaktu = request.POST.get('spos_kontaktu')
        
        # Tu możesz dodać logikę zapisania do bazy danych
        # na przykład: Booking.objects.create(...)
        
        print(f"Rezerwacja: {imie_naz}, {data_od} - {data_do}, {godzina_od} - {godzina_do}")
        print(f"Kontakt: {spos_kontaktu}")
        
        # Wyślij wiadomość e-mail lub zapisz do DB
        
        # Przekieruj na stronę główną lub pokaż komunikat sukcesu
        return redirect('index')  # zmień na swoją główną stronę
        
    except Exception as e:
        print(f"Błąd: {e}")
        return redirect('index')