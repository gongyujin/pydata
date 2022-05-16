from django.urls import path, include
from . import views

app_name='students'
urlpatterns = [
    path('register/',views.register,name='register'),
]

# name='register' 대신 'reg'로 해서 html을 열어도 됨