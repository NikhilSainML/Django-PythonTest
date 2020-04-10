from django.contrib import admin
from django.urls import path
from PythonTest import views

urlpatterns = [
    path('', views.index, name='index'),
    path('execute', views.execute, name='execute')
]
