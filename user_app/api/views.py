from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from user_app.api.serializers import RegisterSerializer
from user_app import models

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.auth.delete()

    return Response(
        {
            "message": "Logout successful"
        },
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        
        token = Token.objects.get(user=user).key

        return Response(
            {
                'token': token,
                'user': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)