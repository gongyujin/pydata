from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('boradList/',views.boardList,name='boardList'),
]
