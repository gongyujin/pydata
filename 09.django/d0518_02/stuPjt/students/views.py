from django.http import HttpResponseRedirect
from django.shortcuts import render
from students.models import Student
from django.urls import reverse

def stuUpdate(request,s_no):
    
    return HttpResponseRedirect(reverse('student:stuUpdate'))



def stuView(request,s_no):
    qs=Student.objects.get(s_no=s_no)
    context={'stu':qs}
    return render(request,'stuView.html',context)


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
    hobby=request.POST.getlist('hobby')
    hobby=','.join(hobby)
    
    Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    print('insert OK')
    
    return HttpResponseRedirect(reverse('students:stuList'))