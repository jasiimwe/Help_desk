from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from account.api.serializer import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registeration_view(request):

    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully created account"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)