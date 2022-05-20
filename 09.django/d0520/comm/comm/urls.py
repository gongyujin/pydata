from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # home연결 - index.html
    path('',include('home.urls')),
    # freeboard app연결
    path('freeboard/',include('freeboard.urls')),
    path('member/',include('member.urls')),
    
]
