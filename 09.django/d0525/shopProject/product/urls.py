from django.urls import path, include
from . import views

app_name='product'
urlpatterns = [
    path('<int:nowpage>/pList/',views.pList,name='pList'),
    path('<int:nowpage>/pWrite/',views.pWrite,name='pWrite'),
]
