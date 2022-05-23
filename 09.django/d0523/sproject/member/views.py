from django.shortcuts import redirect, render
from member.models import Member

# login 함수
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        try:
            # id, pw가 존재할때
            qs=Member.objects.get(id=id,pw=pw)
        except Member.DoesNotExist: 
            # id, pw가 존재하지 않을시
            qs=None

        if qs:
            request.session['session_id'] =qs.id
            request.session['session_nickname']=qs.nickname
            # return render(request,'index.html') # 상단 url 주소가 변경되지 않음.  ==> 메인페이지를 가도 url전체주소가 변겨오디지않음
            return redirect('/') 
        else:
            msg='아이디 또는 패스워드가 일치하지 않습니다. \\n다시 로그인해주세요.!!'
            return render(request,'login.html',{'msg':msg})
            
        
    
# logout 함수 
def logout(request):
    request.session.clear()
        
    return redirect('/')