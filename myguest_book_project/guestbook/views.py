from django.shortcuts import render

from .forms import GuestEntryForm
from .models import GuestEntry, Hit

def home(request):
    if request.method == "POST":
        form = GuestEntryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GuestEntryForm()
    guests = GuestEntry.objects.all()[:10]
    Hit().save()
    hits = Hit.objects.count()
    return render(request, 'guestbook/main.html',
                 {'form': form, 'guests': guests, 'hits': hits})
