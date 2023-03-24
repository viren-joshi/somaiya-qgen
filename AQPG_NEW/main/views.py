from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.core.files.storage import default_storage
from django.conf import settings
from .models import *
from accounts.models import userProfile
from .serializers import *
import os
import json



@api_view(["GET","POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def allquestions(request):
    
    if request.method == "GET":

        course_id = request.GET.get('course_id', None)
        module_id = request.GET.get('module_id', None)

        if course_id == None and module_id == None:
            user = request.user
            ins = userProfile.objects.filter(user=user)
            
            ans = userProfile.objects.none()
            for i in ins:
                ans = ans | Module.objects.filter(course=i.subjectInCharge)
                
            # print(ans)
            items = Post.objects.none()
            for i in ans:
                items = items | Post.objects.filter(module=i)
            # print(items)
            ser = PostSerializer(items, many=True, context={'user': request.user})
            return Response(ser.data)
        else:
            if module_id != None:
                items = Post.objects.filter(module=Module.objects.get(id=module_id))
                ser = PostSerializer(items, many=True, context={'user': request.user})
                return Response(ser.data)
            elif course_id != None:
                ans = Post.objects.none()

                for i in Module.objects.filter(course=Courses.objects.get(id=course_id)):
                    ans = ans | Post.objects.filter(module=i)
                ser = PostSerializer(ans, many=True, context={'user': request.user})
                return Response(ser.data)

    
    elif request.method == "POST":
        data = json.loads(request.body)
        print(data)
       
        d = {
            'module':Module.objects.get(id=data['module_id']),
            'question' : data['question'],
            'questionFile' : data['questionFile'],
            'answer' : data['answer'],
            'marks' : data['marks'],
            'BT_level' : data['BT_level'],
        }

        try:
            ins = Post.objects.get(**d)
            data = {
                "message" : "The Question already Exists"
            }
            return Response(data)
        except:
            pass

        ins = Post.objects.create(**d)
        ins.save()

        data = {
            "message":"Success"
        }

        return Response(data)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload(request):
    f = request.FILES['file']
    file_name = default_storage.save(f.name, f)
    url = os.path.join(settings.MEDIA_URL,file_name)
    data = {
            'slug' : f'http://127.0.0.1:8000{url}',
            'type' : f.content_type
        }
    # print(data)
    return Response(data)




@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def courses(request):

    course_id = request.GET.get('id', None)
    if course_id != None:
        item = Courses.objects.get(id=course_id)
        items = Module.objects.filter(course=item)
        ser = ModuleSerializer(items, many=True)
        return Response(ser.data)
    else:
        user = request.user
        
        ans = []
        
        for i in userProfile.objects.filter(user=user):
            ans.append(Courses.objects.filter(id=i.subjectInCharge.id))

        items = Courses.objects.none()
        for i in ans:
            items = items | i

        ser = CoursesSerializer(items, many=True)
        return Response(ser.data)
    


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def alter(request,action,id):

    user = request.user
    # print(user,type(user))

    try:
        post = Post.objects.get(id=id)
    except:
        d = {
            'message' : f'No Question with id = {id} exists'
        }
        return Response(d)

    if action == 'upvote':
        
        ins = Upvotes.objects.filter(user=user,post=post)
        if len(ins) != 0:
            message = "User has already upvoted"
        else:
            obj = Upvotes.objects.create(user=user,post=post)
            obj.save()
            message = "Success"

    elif action == 'downvote':

        ins = Upvotes.objects.filter(user=user,post=post)
        if len(ins) == 0:
            message = "User has not upvoted"
        else:
            Upvotes.objects.get(user=user,post=post).delete()
            message = "Success"

    elif action == 'flag':
        
        ins = Flag.objects.filter(user=user,post=post)
        if len(ins) != 0:
            message = "User has already Flagged"
        else:
            obj = Flag.objects.create(user=user,post=post)
            obj.save()
            message = "Success"
    
    elif action == 'unflag':

        ins = Flag.objects.filter(user=user,post=post)
        if len(ins) == 0:
            message = "User has not Flagged"
        else:
            Flag.objects.get(user=user,post=post).delete()
            message = "Success"

    elif action == 'bookmark':
        
        ins = Bookmark.objects.filter(user=user,post=post)
        if len(ins) != 0:
            message = "User has already Bookmarked"
        else:
            obj = Bookmark.objects.create(user=user,post=post)
            obj.save()
            message = "Success"

    elif action == 'unbookmark':

        ins = Bookmark.objects.filter(user=user,post=post)
        if len(ins) == 0:
            message = "User has not Bookmarked"
        else:
            Bookmark.objects.get(user=user,post=post).delete()
            message = "Success"

    else:
        message = f"Wrong Action {action}"
        
    d = {
        'message':message
    }
    return Response(d)
    


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request):
    query = request.GET.get('query', None)
    # print(query)

    user = request.user
    ins = userProfile.objects.filter(user=user)
    
    ans = userProfile.objects.none()
    for i in ins:
        ans = ans | Module.objects.filter(course=i.subjectInCharge)
        
    # print(ans)
    items = Post.objects.none()
    for i in ans:
        items = items | Post.objects.filter(module=i)
    # print(items)
    if query != None:
        items = items.filter(question__icontains=query)
    ser = PostSerializer(items, many=True, context={'user': request.user})
    return Response(ser.data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bookmarks(request):
    user = request.user
    items = Bookmark.objects.filter(user=user)
    ser = BookmarkSerializer(items, many=True, context={'user':request.user})
    return Response(ser.data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def modules(request):
    user = request.user
    course = userProfile.objects.get(user=user).subjectInCharge
    items = Module.objects.filter(course=course)
    ser = ModuleSerializer(items, many=True)
    return Response(ser.data)


