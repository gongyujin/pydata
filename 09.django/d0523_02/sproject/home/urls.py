from django.urls import path,include
from . import views

# home설정
app_name=''
urlpatterns = [
    path('',views.index,name='index'),
]
