from django.shortcuts import render
from students.models import Student

# Create your views here.
def register(request):
    
    query= Student(s_name='김구',s_major='정치외교',s_age=25,s_grade=4,s_gender='남자')
    query.save()
    qs1=Student.objects.all()
    print(qs1)
    
    
    qs2=Student.objects.get(s_name='강감찬')
    qs2.delete()
    print('삭제되었습니다.')
    qs3=Student.objects.all()
    print(qs3)
        
    return render(request,'register.html')