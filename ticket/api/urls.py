from django.urls import path, include
from ticket.api.views import (
    api_ticket_detail_view,
    api_update_ticket_view,
    api_delete_ticket_view,
    api_create_ticket_view,
    api_ticket_view
)


app_name = 'ticket'

urlpatterns = [
    path('', api_ticket_view, name='all'),
    path('<int:pk>/', api_ticket_detail_view, name='detail'),
    path('<int:pk>/update', api_update_ticket_view, name='update'),
    path('<int:pk>/delete', api_delete_ticket_view, name='delete'),
    path('create', api_create_ticket_view, name='create'),

    
]