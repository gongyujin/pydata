from django.db import models
from Member.models import Members

class Dailyexercise(models.Model):
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    ex_name=models.CharField(max_length=100)
    ex_time=models.IntegerField(default=0,blank=True) #운동한시간
    burned_kcal=models.IntegerField(default=0,blank=True) # 태운칼로리
    goal_kcal=models.IntegerField(default=1000,blank=True) # 목표칼로리
    createdate=models.DateTimeField(auto_now_add=True) # 등록날짜
    content=models.TextField(blank=True) #세트,횟수 리스트로