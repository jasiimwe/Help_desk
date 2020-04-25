from django.urls import path
from equipment.api.views import (
    api_equipment_detail_view,
    api_update_equipment_view,
    api_delete_equipment_view,
    api_create_equipment_view,
    api_equipment_view
)


app_name = 'equipment'

urlpatterns = [
    path('', api_equipment_view, name='all'),
    path('<int:pk>/', api_equipment_detail_view, name='detail'),
    path('<int:pk>/update', api_update_equipment_view, name='update'),
    path('<int:pk>/delete', api_delete_equipment_view, name='delete'),
    path('create', api_create_equipment_view, name='create'),
]