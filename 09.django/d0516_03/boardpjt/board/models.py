from django.db import models

class Tboard(models.Model):
    bno=models.IntegerField(default=0)
    id=models.CharField(max_length=20)
    btitle=models.CharField(max_length=200)
    bcontent=models.CharField(max_length=3000)
    bdate=models.DateField(auto_now=True)
    bgroup=models.IntegerField(default=0)
    bstep=models.IntegerField(default=0)
    bindent=models.IntegerField(default=0)
    bhit=models.IntegerField(default=0)
    bimg=models.CharField(max_length=200)

    def __str__(self):
	    return self.btitle