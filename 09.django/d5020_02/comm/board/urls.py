from django.urls import path, include
from . import views

app_name='board'
urlpatterns = [
    path('bList/',views.bList,name='bList'),
]
