from django import forms

from .models import GuestEntry


class GuestEntryForm(forms.ModelForm):
	class Meta:
		model = GuestEntry
		fields = ('name',)
