from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    path('stuWrite/',views.stuWrite,name='stuWrite'),
    path('stuWriteOk/',views.stuWriteOk,name='stuWriteOk'),
    path('stuList/',views.stuList,name='stuList'),
    path('<str:s_no>/stuView/',views.stuView,name='stuView'),
    path('<str:s_no>/stuUpdate/',views.stuUpdate,name='stuUpdate'),
]