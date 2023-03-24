from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.core.files.storage import default_storage
from django.conf import settings
from main.models import *
from main.serializers import *
from accounts.models import userProfile
# from .serializers import *
import os
import json
from .generator import get_questions
import random


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generatefrompara(request):
    data = json.loads(request.body)
    ans = get_questions(data['paragraph'])
    

    return Response(ans)

@api_view(["GET","POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generate(request,type_paper):

    # print(request.body)
    

    if type_paper == 'termtest':
        data = json.loads(request.body)
        # print(data)
        
        id_array = data['modules']
        # print(id_array)
        message = "Success"

    elif type_paper == 'endsem' and request.method == "GET":

        user = request.user
        course = userProfile.objects.get(user=user).subjectInCharge
        items = Module.objects.filter(course=course)
        id_array = []
        for i in items:
            id_array.append(i.id)
        # print(id_array)
        message = "Success"

    else:

        message = "Not a valid paper_type"
        data = {
            "message":message
        }
        return Response(data)

    ins_2 = Post.objects.none()
    ins_4 = Post.objects.none()
    ins_8 = Post.objects.none()
    for i in id_array:
        # print(Module.objects.get(id=i))
        # print(i)
        ins_2 = ins_2 | Post.objects.filter(module=Module.objects.get(id=i),marks='2')
        ins_4 = ins_4 | Post.objects.filter(module=Module.objects.get(id=i),marks='4')
        ins_8 = ins_8 | Post.objects.filter(module=Module.objects.get(id=i),marks='8')

    # print(Post.objects.filter(module=Module.objects.get(id=13),marks=2))
    # print('--')
    # print(ins_2)
    # print(PostSerializer(ins_2, many=True).data)
    # print(ins_4)
    # print(ins_8)
    # print('--')
    # ans1 = random.choice(ins_2)
    # ans2 = random.choice(ins_4)
    # ans3 = random.choice(ins_8)

    # print(ans1)
    # print(ans2)
    # print(ans3)
    # ans = ans1 | ans2 | ans3

    ser1 = random.choices(PostSerializer(ins_2, many=True).data,k=8)
    ser2 = random.choices(PostSerializer(ins_4, many=True).data,k=6)
    ser3 = random.choices(PostSerializer(ins_8, many=True).data,k=6)
    
    # ser = PostSerializer(ans, many=True)
    ans = {
        "2" : ser1,
        "4" : ser2,
        "8" : ser3
    }

    return Response(ans)
    


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def questionsinbulk(request):
    data = json.loads(request.body)
    exists = 0
    # print(data)
    for d in data:
        # print(d)
        if Post.objects.filter(**d).exists():
            exists += 1
            print("Exists")
            
        else:
            ins = Post.objects.create(**d)
            ins.save()

    data = {
        "message":"Success",
        "exists":exists
    }

    return Response(data)
        