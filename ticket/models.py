from django.db import models
from account.models import Account
from datetime import datetime

# Create your models here.
category = (
    ('procamis','procamis'),
    ('internet','internet'),
    ('hardware','hardware'),
    ('software','software'),
    ('others','others'),
)
status = (
    
    ('open','open'),
    ('pending','pending'),
    ('resolved','resolved'),
    ('closed','closed'),
)
priority = (
    ('nuetral','nuetral'),
    ('low','low'),
    ('moderate','moderate'),
    ('high','high'),
)


class Ticket(models.Model):
    user = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    ticket_num = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, blank=False, null=False)
    station = models.CharField(max_length=100)
    ticket_category = models.CharField(max_length=100, choices=category)
    description = models.TextField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    ticket_status = models.ForeignKey('TicketStatus', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.ticket_num

class TicketStatus(models.Model):
    #ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status, default='general')
    priority = models.CharField(max_length=100, choices=priority, default='neutral')
    action_taken = models.TextField(max_length=100, null=True)
    technician = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.status


