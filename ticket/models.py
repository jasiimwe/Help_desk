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
    full_name = models.CharField(max_length=200, blank=False, null=False)
    station = models.CharField(max_length=100)
    ticket_category = models.CharField(max_length=100, choices=category)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20, choices=status, default='general')
    priority = models.CharField(max_length=100, choices=priority, default='neutral')
    action_taken = models.TextField(max_length=100, null=True)
    technician = models.CharField(max_length=100, default='General')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    @property
    def ticket_num(self):
        myDate = datetime.now().strftime("%Y")
        
        return "%s-%s" % (self.ticket_category , myDate)

    def __str__(self):
        return self.ticket_num

