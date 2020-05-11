from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from ticket.models import Ticket
from ticket.api.serializer import TicketSerializer

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_ticket_view(request):

    try:
        ticket_detail = Ticket.objects.all()
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = TicketSerializer(ticket_detail, many=True)
        return Response(serializer.data)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_ticket_detail_view(request, pk):

    try:
        ticket_detail = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = TicketSerializer(ticket_detail)
        return Response(serializer.data)

@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
def api_update_ticket_view(request, pk):

    try:
        ticket_detail = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    if ticket_detail.user != user:
        return Response({'response': "You don't have permission to update this ticket"})

    if request.method == "PUT":
        serializer = TicketSerializer(ticket_detail, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))
def api_delete_ticket_view(request, pk):

    try:
        ticket_detail = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    if ticket_detail.user != user:
        return Response({'response': "You don't have permission to delete this ticket"})

    if request.method == "DELETE":
        operation = ticket_detail.delete()
        data = {}
        if operation:
            data["success"] = "delete success"
        else:
            data["error"] = "delete failed"
        return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def api_create_ticket_view(request):
    account = request.user

    ticket = Ticket(user=account)
    if request.method == "POST":
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

