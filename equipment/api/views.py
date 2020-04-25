from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from equipment.models import Equipment
from equipment.api.serializer import EquipmentSerializer

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_equipment_view(request):

    try:
        equipment_detail = Equipment.objects.all()
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = EquipmentSerializer(equipment_detail, many=True)
        return Response(serializer.data)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_equipment_detail_view(request, pk):

    try:
        equipment_detail = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = EquipmentSerializer(equipment_detail)
        return Response(serializer.data)

@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
def api_update_equipment_view(request, pk):

    try:
        equipment_detail = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    if equipment_detail.user != user:
        return Response({'response': "You don't have permission to update this post"})

    if request.method == "PUT":
        serializer = EquipmentSerializer(equipment_detail, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))
def api_delete_equipment_view(request, pk):

    try:
        equipment_detail = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    if equipment_detail.user != user:
        return Response({'response': "You don't have permission to delete this post"})

    if request.method == "DELETE":
        operation = equipment_detail.delete()
        data = {}
        if operation:
            data["success"] = "delete success"
        else:
            data["error"] = "delete failed"
        return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def api_create_equipment_view(request):
    account = request.user

    equipment = Equipment(user=account)
    if request.method == "POST":
        serializer = EquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

