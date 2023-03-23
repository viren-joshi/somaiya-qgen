from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.core.files.storage import default_storage
from django.conf import settings
import os
import json
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status






@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def index(request):
    print('hj')
    # Access any page here
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
        data = {
            'message':'Success',
            'username':username,
            'token':token
        }
        
        return Response(data, status=status.HTTP_202_ACCEPTED)
        
    else:

        data = {
            'message':'Invalid credentials'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    
        

# @csrf_exempt
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def signup(request):
    
    data = json.loads(request.body)
    # name = data['name']
    username = data['username']
    # emailid = data['email']
    password = data['password']

    if User.objects.filter(username=username).exists():
        data = {
            'message':'Username Exists',
            'username':username
        }
        return Response(data,status=status.HTTP_226_IM_USED)

    user = User.objects.create_user(username=username,password=password)
    user.save()

    # client = Client.objects.create(
    #     user=user,
    #     name=name,
    # )
    # client.save()

    data = {
        'message':'User created successfully',
        'username':username
    }

    return Response(data,status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    request.user.auth_token.delete()
    auth_logout(request)
    return Response('User Logged out successfully')


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def uploadfile(request):
    print('hi')
    f = request.FILES['file']
    # data = json.loads(request.body)
    # f = data['file']
    # print(f)
    file_name = default_storage.save(f.name, f)
    url = os.path.join(settings.MEDIA_URL,file_name)
    data = {
            'slug' : f'http://127.0.0.1:8000{url}',
            'type' : f.content_type
        }
    print(data)

    return Response(data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def postquestion(request):
    data = json.loads(request.body)
    question = data['question']
    answer = data['answer']
    file_slug = data['file_slug']
    print('Question', question)
    print('Answer', answer)
    print('file_slug', file_slug)

    data = {
        'message':'Recieved Everything'
    }

    return Response(data)