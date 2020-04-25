from django.urls import path
from .views import (
    create_ticket_view,
    edit_ticket_view,
    get_ticket_detail_view,
    all_ticket_view,
)

urlpatterns = [
    path('', all_ticket_view, name='show_tickets'),
    path('create/', create_ticket_view, name='create_view'),
    path('<int:pk>/edit', edit_ticket_view, name='edit_ticket'),
    path('<int:pk>/', get_ticket_detail_view, name='ticket_detail')
]