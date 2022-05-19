from django.urls import include,path
from . import views

app_name='member'
urlpatterns = [
    path('list/',views.list,name='list'),
    path('login/',views.login,name='login'),
]
