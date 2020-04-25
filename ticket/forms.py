from django import forms
from .models import Ticket

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('full_name', 'station','ticket_category', 'description')

class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('status', 'action_taken','priority', 'technician')

    