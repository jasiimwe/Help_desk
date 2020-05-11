from django import forms
from .models import Ticket

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('full_name', 'ticket_num','station','ticket_category', 'description')


    