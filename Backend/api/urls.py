from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),

    path('courses/',views.addcourse_list,name='addcourse_list'),
    path('courses/<int:pk>/', views.addcourse_detail, name='addcourse_detail'),

    path('modules/',views.addmodule_list,name='addmodule_list'),
    path('modules/<int:pk>/', views.addmodule_detail, name='addmodule_detail'),

    path('topics/',views.addtopic_list,name='addtopic_list'),
    path('topics/<int:pk>/', views.addtopic_detail, name='addtopic_detail'),
    
    path('questions/',views.addquestion_list,name='addquestion_list'),
    path('questions/<int:pk>/', views.addquestion_detail, name='addquestion_detail'),

    path('generatemcq/',views.generatemcq,name='mcq'),
    # path('multiplemcq/',views.multiplemcq,name='multiplemcq'),

    # path('upload/',views.upload,name='upload'),

    path('questions/upvote/',views.upvote,name='upvote'),
    path('questions/bookmark/',views.bookmark,name='bookmark'),
    path('questions/flag/',views.flag,name='flag'),

    path('addquestions/',views.addaftergeneration,name='addaftergeneration'),


    path('uploadfile/',views.uploadfile, name='uploadfile'),
    # path('postquestion/',views.postquestion, name='uploadfile'),
]