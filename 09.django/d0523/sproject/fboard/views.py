from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F

# 게시판 수정
def fUpdate(request,f_no):
    # form 데이터 전달
    if request.method=='GET':
        qs=Fboard.objects.get(f_no=f_no)
        context={'board':qs}
        return render(request,'fUpdate.html',context)
    else:
        # 수정 form에서 데이터 전달
        id=request.POST.get('id')
        title=request.POST.get('title')
        content=request.POST.get('content')
        file=request.POST.get('file',None)
        # db에 수정저장
        qs=Fboard.objects.get(f_no=f_no)
        qs.f_title=title
        qs.f_content=content
        qs.f_file=file
        qs.save()
        return redirect('fboard:fList')
        


# 게시판 삭제
def fDelete(request,f_no):
    qs=Fboard.objects.get(f_no=f_no)
    qs.delete()
    
    return redirect('fboard:fList')


# 게시판 답글쓰기 함수
def fReply(request,f_no):
    if request.method=='GET':
        qs=Fboard.objects.get(f_no=f_no)
        context={'board':qs}
        return render(request,'fReply.html',context)
    else:
        # id 숨겨야함
        id=request.POST.get('id')
        # id=request.session.session_id
        print('id: ',id)
        # request 넘어온 데이터타입: str타입
        member=Member.objects.get(id=id)
        group=int(request.POST.get('group'))
        step=int(request.POST.get('step'))
        indent=int(request.POST.get('indent'))
        
        title=request.POST.get('title')
        content=request.POST.get('content')
        file=request.POST.get('file',None)
        
        # # 부모 group에서 부모보다 큰 step 찾아서 1씩 증가, gt : 보다 큰 수
        # reboard=Fboard.objects.filter(f_group=group,f_step_gt=step)
        # # F참조객체: db에서 검색을 해서 가져올 수 있음.
        # reboard.update(f_step=F('f_step')+1)
        Fboard.objects.filter(f_group=group,f_step__gt=step).update(f_step=F('f_step')+1)
        
        
        # 처음에 부모보다 +1, step들어 오는 수보다 큰것들은 다 +1해줌
        # step: 출력순서, indent: 들여쓰기
        qs=Fboard(member=member,f_title=title,f_content=content,f_group=group,f_step=step+1,f_indent=indent+1,f_file=file)
        qs.save() # f_no
        
        
        return redirect('fboard:fList')
        
        

# 게시판 읽기 함수
def fView(request,f_no):
    qs=Fboard.objects.get(f_no=f_no)
    context={'board':qs}
    
    return render(request,'fView.html',context)


# 게시판 글쓰기 함수
def fWrite(request):
    if request.method=='GET':
        return render(request,'fWrite.html')
    else:
        # form에서 넘어온 데이터
        id=request.POST.get('id')
        member=Member.objects.get(id=id)
        title=request.POST.get('title')
        content=request.POST.get('content')
        file=request.POST.get('file',None)
        # db저장
        qs=Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group=qs.f_no
        qs.save()        

        # url주소를 refresh해서 fList로 보냄
        return redirect('fboard:fList')


# 게시판 리스트 함수
def fList(request):
    qs=Fboard.objects.order_by('-f_group','f_step')
    context={'fList':qs}
    return render(request,'fList.html',context)