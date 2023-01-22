from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .models import *
from django.core.files.storage import default_storage
from django.conf import settings
import os
import json

from .main import generate_mcq


# @csrf_exempt
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    d = {
        'message' : "Index Page"
    }
    return JsonResponse(d)


# @csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addcourse_list(request):
    if request.method == 'GET':
        course_id = request.GET.get('id', None)
        if course_id != None:
            item = Courses.objects.get(id=course_id)
            res = list(item.modules.all())
            data = {}
            for x in res:
                data[x.name] = {'id' : x.id, 'name' : x.name}
            # print('d',data)
            return JsonResponse(data)
            
        items = Courses.objects.order_by("pk")
        ser = CoursesSerializer(items, many=True)
        return Response(ser.data)
    elif request.method == 'POST':
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# @csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def addcourse_detail(request,pk):
    try:
        item = Courses.objects.get(pk=pk)
    except Courses.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CoursesSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CoursesSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


# @csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def addmodule_list(request):
    if request.method == 'GET':
        items = Module.objects.order_by("pk")
        ser = ModuleSerializer(items, many=True)
        return Response(ser.data)
    elif request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def addmodule_detail(request):
    pass


# @csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addtopic_list(request):
    if request.method == 'GET':
        items = Topics.objects.order_by("pk")
        ser = TopicsSerializer(items, many=True)
        return Response(ser.data)
    elif request.method == 'POST':
        serializer = TopicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def addtopic_detail(request):
    pass


# @csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addquestion_list(request):

    print('hi')
    if request.method == 'GET':
        module_id = request.GET.get('module_id', None)
        course_id = request.GET.get('course_id', None)
        uID = request.GET.get('uID', None)
        # print(module_id,course_id)
        print(uID)
        

        items = Questions.objects.order_by("pk")
        ser = QuestionsSerializer(items, many=True,context={'uID': uID})
        # print(ser.data)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # enctype="multipart/form-data"
        print(request.data)
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print('Error',serializer.errors)
        return Response(serializer.errors, status=400)

@csrf_exempt
def addquestion_detail(request):
    pass

# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generatemcq(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data['paragraph']
        
        data = generate_mcq(text)
        for x in data['mcqs']:
            print(x)
        return JsonResponse(data)
    return HttpResponse('Method not allowed')



# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addaftergeneration(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        # mcq = data['mcq']
        # bt = data['bt']


        Questions.objects.create(
            question='It does this by using Data Mining algorithms to identify what is deemed knowledge.The Knowledge Discovery in  ___  is considered as a programmed, exploratory analysis and modeling of vast data repositories.KDD is the organized procedure of recognizing valid, useful, and understandable patterns from huge and complex data sets.',
            option_1="Course Of Study",
            option_2="Ammunition",
            option_3="Confirmation",
            option_4="Databases",
            type=0
        )

        Questions.objects.create(
            question="Explain in brief data mining",
            type=1
        )



        
        # data = generate_mcq(text)
        # for x in data['mcqs']:
        #     print(x)
        # return JsonResponse(data)
        return HttpResponse("SUccess")
    return HttpResponse('Method not allowed')

# @csrf_exempt
# @api_view(['POST'])
# def multiplemcq(request):
#     if request.method == 'POST':
#         for item in request.data['mcqs']:
#             # print(item)
#             serializer = MCQSerializer(data=item)
#             if serializer.is_valid():
#                 serializer.save()
#             else:
#                 print('A mcq has wrong data types')
#         return Response({'Status':"Success"}, status=201)
#     return Response(serializer.errors, status=400)
    


# @csrf_exempt
# def upload(request):
#     # enctype="multipart/form-data"
#     if request.method == 'POST':
#         f = request.FILES['file']
        
#         file_name = default_storage.save(f.name, f)
#         url = os.path.join(settings.MEDIA_URL,file_name)
#         data = {
#             'slug' : url,
#             'type' : f.content_type
#         }
#         return JsonResponse(data)
#     pass


# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upvote(request):


    if request.method == 'POST':
        data = json.loads(request.body)
        u_id = data['user_id']
        q_id = data['question_id']
        print(data)

        if data['function'] == 'add_upvote':

            instance = upvote_check.objects.filter(user_id=u_id)
            if instance.exists():
                
                if q_id in instance[0].question_id:
                    return HttpResponse('You get only 1 Upvote')
                else:
                    instance = upvote_check.objects.get(user_id=u_id)
                    instance.question_id.append(int(q_id))
                    instance.save()
            else:
                obj = upvote_check.objects.create(user_id=u_id)
                obj.question_id = [q_id]
                obj.save()

            obj = Questions.objects.get(id=data['question_id'])
            obj.upvotes += 1
            obj.save()

        elif data['function'] == 'remove_upvote':

            try:
                obj = upvote_check.objects.get(user_id=u_id)
                if q_id in obj.question_id:
                    obj.question_id.remove(q_id)
                    obj.save()
                else:
                    return HttpResponse("You have not upvoted yet")

                obj = Questions.objects.get(id=data['question_id'])
                obj.upvotes -= 1
            except Exception as e:
                print(e)
                return HttpResponse('You can not downvote without upvoting')


        else:
            return HttpResponse("Wrong schema of request.body")
        
        return HttpResponse("Success !!")


    return HttpResponse('Method not allowed')



# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bookmark(request):


    if request.method == 'POST':
        data = json.loads(request.body)
        u_id = data['user_id']
        q_id = data['question_id']
        print(data)

        if data['function'] == 'add_bookmark':
            
            instance = bookmarks.objects.filter(user_id=u_id)
            if instance.exists():
                if q_id in instance[0].question_id:
                        return HttpResponse('You have already bookmarked !!')
                else:
                    instance = bookmarks.objects.get(user_id=u_id)
                    instance.question_id.append(int(q_id))
                    instance.save()
            else:
                obj = bookmarks.objects.create(user_id=u_id)
                obj.question_id = [q_id]
                obj.save()

        elif data['function'] == 'remove_bookmark':

            try:
                obj = bookmarks.objects.get(user_id=u_id)
                if q_id in obj.question_id:
                    obj.question_id.remove(q_id)
                    obj.save()
                else:
                    return HttpResponse("You have not bookmarked that yet")

            except Exception as e:
                print(e)
                return HttpResponse('You can not Remove a Bookmark without adding it')


        else:
            return HttpResponse("Wrong schema of request.body")


        return HttpResponse("Success !!")
        
    return HttpResponse("Method not allowed")




# @csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def flag(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        u_id = data['user_id']
        q_id = data['question_id']
        print(data)

        if data['function'] == 'add_flag':
            
            instance = flag_check.objects.filter(user_id=u_id)
            if instance.exists():
                if q_id in instance[0].question_id:
                        return HttpResponse('You have already bookmarked !!')
                else:
                    instance = flag_check.objects.get(user_id=u_id)
                    instance.question_id.append(int(q_id))
                    instance.save()
            else:
                obj = flag_check.objects.create(user_id=u_id)
                obj.question_id = [q_id]
                obj.save()

        elif data['function'] == 'remove_flag':

            try:
                obj = flag_check.objects.get(user_id=u_id)
                if q_id in obj.question_id:
                    obj.question_id.remove(q_id)
                    obj.save()
                else:
                    return HttpResponse("You have not bookmarked that yet")

            except Exception as e:
                print(e)
                return HttpResponse('You can not Remove a Bookmark without adding it')


        else:
            return HttpResponse("Wrong schema of request.body")


        return HttpResponse("Success !!")
        
    return HttpResponse("Method not allowed")





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
            'slug' : f'{url}',
            'type' : f.content_type
        }
    print(data)

    return Response(data)


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# def postquestion(request):
#     data = json.loads(request.body)
#     question = data['question']
#     answer = data['answer']
#     file_slug = data['file_slug']
#     print('Question', question)
#     print('Answer', answer)
#     print('file_slug', file_slug)

#     data = {
#         'message':'Recieved Everything'
#     }

#     return Response(data)