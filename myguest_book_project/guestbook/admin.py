from django.contrib import admin

from .models import GuestEntry
from .models import Hit

admin.site.register(GuestEntry)
admin.site.register(Hit)

