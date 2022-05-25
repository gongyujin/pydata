from django.shortcuts import redirect, render
from member.models import Member
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        try:
            qs=Member.objects.get(id=id,pw=pw)
            
        except Member.DoesNotExist:
            qs=None

        if qs:
            request.session['session_id']=qs.id
            request.session['session_nickname']=qs.nickname
            return redirect('/')
        else:
            msg='아이디 또는 패스워드가 일치하지 않습니다. \\n다시 입력하세요.'            
            return render(request,'login.html',{'msg':msg})


def logout(request):
    request.session.clear()
    return redirect('/')