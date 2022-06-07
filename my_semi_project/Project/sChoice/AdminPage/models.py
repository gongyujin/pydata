from django.db import models

# 운동db
class Exercise(models.Model):
    ex_id=models.CharField(max_length=20,primary_key=True)
    ex_name=models.CharField(max_length=300)    
    activity=models.CharField(max_length=100)
    level=models.IntegerField(default=2)
    met=models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.ex_id
    
    # user_id = models.CharField(max_length=20,primary_key=True)
    # user_pw = models.CharField(max_length=100)
    # user_name = models.CharField(max_length=100)
    # pro = models.IntegerField(default=0)
    # birth = models.DateField(blank=True)
    # gender = models.CharField(max_length=10,blank=True)
    # phone = models.CharField(max_length=13,blank=True)
    # zipcode = models.CharField(max_length=6,blank=True)
    # addressd1=models.CharField(max_length=1000,blank=True)
    # addressd2=models.CharField(max_length=1000,blank=True)
    # user_purpose = models.CharField(max_length=1000,blank=True)
    # service = models.CharField(max_length=1000,blank=True)
    # vegan = models.IntegerField(default=0)
    # allergic_food = models.CharField(max_length=1000,blank=True)
    # goal_wieght = models.IntegerField(default=55)
    # goal_bodyfat = models.IntegerField(default=25)
    # createdate=models.DateTimeField(auto_now_add=True)
    # modidate=models.DateTimeField(auto_now=True)