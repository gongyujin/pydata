from django.shortcuts import render
from fboard.models import Fboard

def event(request):
    return render(request,'event.html')


def event_view(request):
    print("f_no : ",request.GET.get('f_no'))
    return render(request,'event_view.html')

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