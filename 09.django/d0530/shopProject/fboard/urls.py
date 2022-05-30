from django.urls import path,include
from . import views

app_name='fboard'
urlpatterns = [
    path('fList/',views.fList,name='fList'),
    path('list/',views.list,name='list'),
    path('event/',views.event,name='event'),
    path('event_view/',views.event_view,name='event_view'),
]
