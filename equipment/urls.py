from django.urls import path, include
from .views import (
    equipment_view,
    equipment_create,
    edit_equipment,
    equipment_detail_view,
    )


urlpatterns = [
    path('', equipment_view, name='show_equipment'),
    path('create/', equipment_create, name='create_equipment'),
    path('<int:pk>/edit', edit_equipment, name='edit_equipment'),
    path('<int:pk>/', equipment_detail_view, name='equipment_detail'),

    #api urls
    path('api/', include('equipment.api.urls', 'equipment_api'))
    
]

