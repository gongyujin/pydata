from django.urls import include, path
from . import views

app_name='product'
urlpatterns = [
    path('pWrite/',views.pWrite,name='pWrite'),
    path('pList/',views.pList,name='pList'),
    path('<str:p_no>/pUpdate/',views.pUpdate,name='pUpdate'),
]
