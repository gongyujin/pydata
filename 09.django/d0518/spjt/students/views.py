from django.http import HttpResponseRedirect
from django.shortcuts import render
from students.models import Student
from django.urls import reverse

# 학생삭제 함수
def stuDelete(request,s_no):
    qs=Student.objects.get(s_no=s_no)
    qs.delete()
    
    return HttpResponseRedirect(reverse('students:stuList'))


# 학생수정저장 함수
def stuUpdateOk(request):
    # form 데이터 가져오기
    s_no=request.POST.get('s_no')
    major=request.POST.get('major')
    age=request.POST.get('age')
    grade=request.POST.get('grade')
    gender=request.POST.get('gender')
    hobby=request.POST.getlist('hobby') 
    hobby=','.join(hobby) # list타입 -> str 타입
    
    # s_no 데이터 찾기
    qs=Student.objects.get(s_no=s_no)
    qs.s_major=major
    qs.s_age=age
    qs.s_grade=grade
    qs.s_gender=gender
    qs.s_hobby=hobby
    # 데이터 수정저장
    qs.save()
    
    return HttpResponseRedirect(reverse('students:stuList'))

# 학생수정 함수
def stuUpdate(request,s_no):
    qs=Student.objects.get(s_no=s_no)
    context={'stu':qs}
    return render(request,'stuUpdate.html',context)


# 학생상세함수
def stuView(request,s_no):
    # s_no를 가지고 데이터 검색
    qs=Student.objects.get(s_no=s_no)
    context={'stu':qs}
    
    return render(request,'stuView.html',context)


# 학생전체리스트 함수
def stuList(request):
    # db전체데이터 가져오기 : order_by: 정렬, -는 역순정렬  // order_by대신 숫자로 순차정렬할때는 all()
    qs=Student.objects.order_by('-s_no')
    count=qs.count() # 학생전체리스트 개수
    context = {'stuList':qs,'count':count} # context는 항상 dict형태로 보내줘야함
    return render(request,'stuList.html',context)



# 학생등록함수
def stuWrite(request):
    
    return render(request,'stuWrite.html')


# 학생등록저장함수
def stuWriteOk(request):
    name=request.POST.get('name') # data가 넘어오지 않으면 none
    # s_name=request.POST['name'] # data가 넘어오지 않으면 error
    major=request.POST.get('major')
    age=request.POST.get('age')
    grade=request.POST.get('grade')
    gender=request.POST.get('gender')
    # ss_hobby=request.POST.get('hobby') # getlist가 아닌 get으로 받으면 list의 마지막만 넘어옴
    hobby=request.POST.getlist('hobby') # hobby배열형태로 넘어옴    
    # db에는 CharField로 저장되어야함, 현재 s_hobby는 list타입으로 저장이 되지 않음
    # ==> 리스트 타입인 s_hobby를 str타입으로 변경해야함
    # s_hobby list:  ['게임', '골프', '수영', '독서'] 
    # print("s_hobby list : ",s_hobby)
    hobby=','.join(hobby) # list타입 -> str 타입
    # print("s_hobby join : ",hobby)
    # print("s_hobby join 타입 : ",type(s_hobby))
    # ss_hobby=s_hobby.split(',') # str타입 -> list타입
    # print('ss_hobby : ', ss_hobby)
    # print('ss_hobby 타입 : ', type(ss_hobby))
    
    # db에 저장 -> sqlite3 table insert명령어
    Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    # qs=Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    # qs.save()
    print("insert OK")
    
    
    return HttpResponseRedirect(reverse('students:stuList'))