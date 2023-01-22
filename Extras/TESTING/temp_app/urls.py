
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('uploadfile/',views.uploadfile, name='uploadfile'),
    path('postquestion/',views.postquestion, name='uploadfile'),

]
