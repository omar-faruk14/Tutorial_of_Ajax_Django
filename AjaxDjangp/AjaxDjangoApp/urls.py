from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeCrued.as_view(), name='home'),
    path('DataSave/',views.UserInfoSave.as_view(),name="dataSave")
    
]
