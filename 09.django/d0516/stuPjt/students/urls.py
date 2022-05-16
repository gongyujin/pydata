from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    # students/register/
    # students/update/
    path('register/',views.register,name='register'),
]
