from django.db import models
from datetime import datetime


class Member(models.Model):
    m_no=models.AutoField(primary_key=True)
    m_id=models.CharField(max_length=100)
    m_pw=models.CharField(max_length=100)
    m_name=models.CharField(max_length=200)
    m_tel=models.CharField(max_length=13)
    m_zip=models.CharField(max_length=5)
    m_adress1=models.CharField(max_length=300)
    m_adress2=models.CharField(max_length=300)
    m_date=models.DateTimeField(default=datetime.now(),blank=True)
    
    
    def __str__(self):
        return self.m_id
    