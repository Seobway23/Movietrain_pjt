from django.shortcuts import render
from .serializer import UserProfileSerializer, UserDetailSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.authtoken.models import Token

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_profile(request, user_pk):
#     if request.method =='GET':
#         user = User.objects.get(pk=user_pk)
#         serializer  = UserProfileSerializer(user)

#         return Response(serializer.data)
    

@api_view(['GET','DELETE', 'PUT'])
def user_profile(request, username):
    username = User.objects.get(request.user)
    if request.method =='GET':
        serializer  = UserProfileSerializer(username)
        return Response(serializer.data)

    if request.method =='DELETE':
        username.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = UserDetailSerializer(username, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def find_username(request):
    token = Token.objects.get(token=request.token)
    user = token.user
    
    
