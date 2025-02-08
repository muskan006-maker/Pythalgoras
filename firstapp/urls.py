from django.urls import path
from firstapp import views
from django.shortcuts import render

urlpatterns = [
    path('',views.firstappview),
    path('view2/',views.firstappview2),
    path('view3/',views.firstappview3),
    path('view4/',views.fourthview),
    path('view5/', views.fifthview, name='view5'), 


]