from django.contrib import admin
from students.models import Student
# Register your models here.

# admin페이지에서 컬럼을 추가하는 방법
@admin.register(Student)
class StudentAmin(admin.ModelAdmin):
    list_display=['s_no','s_name','s_major','s_age']

# admin.site.register(Student,StudentAmin)