from datetime import datetime
from django.db import models

class Board(models.Model):
    b_no=models.AutoField(primary_key=True)
    id=models.CharField(max_length=100)
    b_title=models.CharField(max_length=1000)
    b_content=models.TextField()
    b_group=models.IntegerField(default=0)
    b_indent=models.IntegerField(default=0)
    b_step=models.IntegerField(default=0)
    b_creatdate=models.DateTimeField(default=datetime.now(),blank=True)
    b_updatedate=models.DateTimeField(default=datetime.now(),blank=True)
    b_hit=models.IntegerField(default=0)
    
    def __str__(self):
        return self.b_title