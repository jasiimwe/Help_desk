from rest_framework import serializers
from equipment.models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Equipment
        fields = ('equipment_type','serial_number','station','user_assesment',
        'current_condition','recommendation','current_location','delivered_by',
        'phone_number','status','created_at',
         'username')

        
    def get_username_from_author(self, equipment):
        username = equipment.user.username
        return username