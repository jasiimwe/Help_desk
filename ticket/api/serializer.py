from rest_framework import serializers
from ticket.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Ticket
        fields = ('full_name', 'station','ticket_category', 'description','status',
         'action_taken','priority', 'technician', 'created_at', 'username')

        
    def get_username_from_author(self, ticket):
        username = ticket.user.username
        return username