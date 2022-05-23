from django.db import models
from datetime import datetime
from member.models import Member

class Fboard(models.Model):
    f_no=models.AutoField(primary_key=True)
    ## primary key : Member객체 => id는 1개 컬럼으로 받는데, ForeignKey는 Member으로 객체로 받음
    # id만을 저장하지만 뽑을 때 member객체를 보여줄 수 있게 자동변환시켜줌 ==> 객체를 db에 저장시킬 수 있게 구현됨
    member=models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    # id=models.CharField(max_length=100)
    f_title=models.CharField(max_length=1000)
    f_content=models.TextField()
    f_group=models.IntegerField(default=0)
    f_step=models.IntegerField(default=0)
    f_indent=models.IntegerField(default=0)
    f_hit=models.IntegerField(default=1)
    f_creatdate=models.DateTimeField(default=datetime.now(),blank=True)
    f_updatedate=models.DateTimeField(default=datetime.now(),blank=True)
    f_file=models.ImageField(blank=True)

    def __str__(self):
        return self.f_title    
    