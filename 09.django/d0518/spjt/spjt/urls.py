from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/students/
    path('students/',include('students.urls')),
    path('',include('home.urls')),
    path('member/',include('member.urls')),
]
