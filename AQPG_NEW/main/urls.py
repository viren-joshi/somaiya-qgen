from django.urls import path
from . import views

urlpatterns = [
    path('',views.allquestions,name='allquestions'),
    path('courses/',views.courses,name='courses'),
    path('modules/',views.modules,name='modules'),
    path('upload/',views.upload,name='upload'),
    path('alter/<str:action>/<int:id>',views.alter,name='alter'),
    path('search/',views.search,name='search'),
    path('bookmarks/',views.bookmarks,name='bookmarks'),
    
    
]
