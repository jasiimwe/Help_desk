from django.contrib import admin
from .models import Ticket, TicketStatus


# Register your models here.
#class TicketAdmin(admin.ModelAdmin):
    #list_display('full_name','station','status','priority','action_taken','created_at')


admin.site.register(Ticket)
admin.site.register(TicketStatus)