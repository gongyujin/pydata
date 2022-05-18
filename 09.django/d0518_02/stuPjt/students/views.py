from django.http import HttpResponseRedirect
from django.shortcuts import render
from students.models import Student
from django.urls import reverse

def stuList(request):
    qs=Student.objects.order_by('-s_no')
    count=qs.count()
    context={'stuList':qs, 'count':count}
    return render(request,'stuList.html',context)


def stuWrite(request):
    return render(request,'stuWrite.html')

def stuWriteOk(request):
    name=request.POST.get('name')
    major=request.POST.get('major')
    age=request.POST.get('age')
    grade=request.POST.get('grade')
    gender=request.POST.get('gender')
    hobby=request.POST.get('hobby')
    hobby=','.join(hobby)
    
    Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    print('insert OK')
    
    return HttpResponseRedirect(reverse('students:stuList'))