from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
import json



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def checkstatus(request):
    # Check if user is authenticated
    data = {
        'message':"You are authenticated"
    }
    return Response(data,status=status.HTTP_200_OK)



@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def login(request):

    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        token = Token.objects.get_or_create(user=user)[0].key
        # print(token)
        auth_login(request,user)

        user_type = []
        for i in userProfile.objects.filter(user=user):
            if i.userType not in user_type:
                user_type.append(i.userType)

        data = {
            'message':'Success',
            'username':username,
            'user_type':user_type[0],
            'token':token
        }
        
        return Response(data, status=status.HTTP_202_ACCEPTED)
        
    else:

        data = {
            'message':'Invalid credentials'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    request.user.auth_token.delete()
    auth_logout(request)
    return Response('User Logged out successfully')

