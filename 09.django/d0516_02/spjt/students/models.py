from django.db import models

# Student클래스 선언
class Student(models.Model):
    # 한글은 3바이트, 영어는 2바이트
    # 오라클에서 s_name varchar2(100) 해준것과 같은 의미
    s_name = models.CharField(max_length=100) # 문자(varchar2)
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0) # 정수
    s_grade = models.IntegerField(default=0) # 정수
    s_gender = models.CharField(max_length=3) # 문자
    s_date = models.DateField(auto_now=True) # 날짜
    
    def __str__(self):
        return self.s_name
    
