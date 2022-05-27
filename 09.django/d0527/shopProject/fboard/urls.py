from django.urls import path,include
from . import views

app_name='fboard'
urlpatterns = [
    path('fList/',views.fList,name='fList'),
    path('list/',views.list,name='list'),
]
