from django.shortcuts import render
from fboard.models import Fboard

def list(request):
    qs=Fboard.objects.all()
    count=qs.count
    context={'fList':qs,'count':count}
    return render(request,'list.html',context)



def fList(request):
    qs=Fboard.objects.all()
    count=qs.count
    context={'fList':qs,'count':count}
    return render(request,'fList.html',context)