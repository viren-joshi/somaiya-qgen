from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.questionsinbulk,name='questionsinbulk'),
    path('generatefrompara/',views.generatefrompara,name='generatefrompara'),
    path('generate/<str:type_paper>/',views.generate,name='generate'),

    
]
