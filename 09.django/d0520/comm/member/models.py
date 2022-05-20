from django.db import models
from datetime import datetime


class Member(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pw=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    nickname=models.CharField(max_length=100)
    tel=models.CharField(max_length=13)
    zipcode=models.CharField(max_length=6)
    address1=models.CharField(max_length=300)
    address2=models.CharField(max_length=300)
    gender=models.CharField(max_length=10)
    hobby=models.CharField(max_length=100)
    creatdate=models.DateTimeField(default=datetime.now(),blank=True)
    updatedate=models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.id