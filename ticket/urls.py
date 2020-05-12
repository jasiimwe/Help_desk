from django.urls import path, include
from .views import (
    #create_ticket_view,
    edit_ticket_view,
    get_ticket_detail_view,
    all_ticket_view,
    CreateTicketView,
    TicketDetailView,
)
app_name = 'ticket'

urlpatterns = [
    path('', all_ticket_view, name='show_tickets'),
    path('create/', CreateTicketView.as_view(), name='create_ticket'),
    path('<int:pk>/edit', edit_ticket_view, name='edit_ticket'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),

    #api urls
    path('api/', include('ticket.api.urls', 'ticket_api'))
]