from django.contrib import admin
# Student 클래스를 import
from students.models import Student
# Register your models here.

admin.site.register(Student)