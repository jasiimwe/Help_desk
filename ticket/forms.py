from django import forms
from .models import Ticket, TicketStatus

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('full_name', 'ticket_num','station','ticket_category', 'description')

class TicketStatusForm(forms.ModelForm):
    class Meta:
        model = TicketStatus
        fields = ('ticket','status', 'priority', 'action_taken','technician')


    