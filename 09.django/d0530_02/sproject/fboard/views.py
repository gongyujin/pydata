from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from urllib3 import HTTPResponse
from fboard.models import Fboard,Comment
from member.models import Member
from django.db.models import F,Q
from django.core.paginator import Paginator
from django.core import serializers

# 댓글수정저장
def commUpdateOk(request):
    c_no=request.GET.get('c_no')
    c_content=request.GET.get('c_content')
    id=request.session.get('session_id')
    
    print("commUpdateOk : ",c_no,c_content,id)
    # 해당데이터 검색
    qs=Comment.objects.get(c_no=c_no)
    qs.c_content=c_content
    qs.c_date=datetime.now()
    qs.save()
    
    # ajax으로 전송
    context={'c_no':c_no,'c_content':c_content,'c_date':qs.c_date,'result':'댓글이 수정되었습니다.'}
    return JsonResponse(context) 


def commDelete(request):
    c_no=request.GET.get('c_no')
    qs=Comment.objects.get(c_no=c_no)
    qs.delete()
    context={'result':'댓글이 삭제되었습니다.'}
    return JsonResponse(context) # json은 무조건 string형태로 넘어감

# 댓글 write ==> query 형태로 들어옴 ; 딕셔너리 형태로 넘겨줌
def commWrite(request):
    # html 페이지에서 데이터 가져오기
    f_no=request.GET.get('f_no')
    fboard=Fboard.objects.get(f_no=f_no)
    pw=request.GET.get('pw')
    content=request.GET.get('content')
    id=request.session.get('session_id')
    member=Member.objects.get(id=id)
    
    # db에 저장
    qs=Comment(member=member,fboard=fboard,c_pw=pw,c_content=content)
    qs.save()
    # 댓글번호 넘겨줌
    c_no=qs.c_no
    c_date=qs.c_date
    # 저장데이터 : c_no, member, fboard, c_content,c_date,c_pw
    context={'c_no':c_no,'f_no':f_no,'c_pw':pw,'c_content':content,'c_date':c_date}
    return JsonResponse(context)



# 댓글list ==> query set 형태로 들어옴; list형태로 넘겨줌
def commList(request):
    f_no=request.GET.get('f_no')
    print('f_no commList: ',f_no)
    # f_no 하단댓글을 검색
    qs=Comment.objects.filter(fboard=f_no).order_by('-c_no')
    # list타입으로 전송 : safe=False
    clist=list(qs.values()) # [0:q1,1:q2,2:q3]
    return JsonResponse(clist,safe=False) #safe=False: list타입모양으로 리턴한다는 의미
    # # return HttpResponse('<html><h2>테스트</h2></html>')

    # # HTTPResponse : json형 변환 - dic 타입
    # clist=serializers.serialize('json',qs)
    # return HttpResponse(clist,content_type='text/json-comment-filtered')
    
    
    # # Jsonresponse: dic타입으로 전송
    # # context={'reload_all':False,'clist':clist}
    # context={'clist':clist}
    # return JsonResponse(context)




# 이벤트뷰 함수
def event_view(request):
    print("f_no : ",request.GET.get('f_no'))
    # GET으로 받은 f_no를 넘겨줌
    context={'f_no':request.GET.get('f_no')}
    return render(request,'event_view.html',context)

# 이벤트함수
def event(request):
    return render(request,'event.html')

# 게시판 수정 함수
def fUpdate(request,f_no,nowpage,category, searchword):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no)
        context = {'board':qs,'nowpage':nowpage,'category':category,'searchword':searchword}
        return render(request,'fUpdate.html',context)
    else:
        # 수정form에서 데이터 전달
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        # file = request.POST.get('file',None)
        # 1.기존 파일이 첨부됨
        # 2.파일을 새롭게 등록은 하지 않음
        # 3.none이 들어가게됨
        file = request.FILES.get('file',None)
        
        # db에 수정저장
        qs = Fboard.objects.get(f_no=f_no)
        qs.f_title = title
        qs.f_content = content
        if file: # 파일등록이 되었으면 저장함
            qs.f_file = file
        
        qs.save()
        return redirect('fboard:fList',nowpage,category, searchword)

# 게시판 삭제 함수
def fDelete(request,f_no,nowpage,category, searchword):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage,category, searchword)

# 게시판 답글쓰기 함수
def fReply(request,f_no,nowpage,category,searchword):
    if request.method == 'GET':
        qs = Fboard.objects.get(f_no=f_no) 
        context={'board':qs,'nowpage':nowpage,'category':category,'searchword':searchword}
        return render(request,'fReply.html',context)
    else:
        # id = request.session.session_id
        id = request.POST.get('id')
        print("id:",id)
        member = Member.objects.get(id=id)
        # request 넘어온 데이터타입 : str타입
        group = int(request.POST.get('group'))
        step = int(request.POST.get('step'))
        indent = int(request.POST.get('indent'))
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file',None)
        
        # 부모group에서 부모보다 큰 step 1씩증가, gt보다 큰수
        # reboard = Fboard.objects.filter(f_group=group,f_step_gt=step)
        # # F참조객체: db에서 검색을 해서 가져올수 있음.
        # reboard.update(f_step=F('f_step')+1)
        
        # 부모group에서 부모보다 큰 step 1씩증가, gt보다 큰수
        # F참조객체: db에서 검색을 해서 가져올수 있음.
        Fboard.objects.filter(f_group=group,f_step__gt=step).update(f_step=F('f_step')+1)
        
        # step: 출력순서, indent: 들여쓰기
        qs=Fboard(member=member,f_title=title,f_content=content,f_group=group\
            ,f_step=step+1,f_indent=indent+1,f_file=file)
        qs.save() # f_no
        
        return redirect('fboard:fList',nowpage,category,searchword)

    

# 게시판 읽기 함수
def fView(request,f_no,nowpage,category,searchword):
    qs = Fboard.objects.get(f_no=f_no)
    
    # 게시판리스트 - f_group역순정렬, f_step 순차정렬
    # 이전글: 답글로 게시글이 등록될때 찾을 수 있는 검색
    try:
        qs_next=Fboard.objects.filter(f_group=qs.f_group,f_step__lt=qs.f_step).order_by('-f_group','f_step').last().f_no
    except:
        # 순차적으로 게시글이 등록될때 찾을 수 있는 이전글 검색
        try:
            qs_next=Fboard.objects.filter(f_group__gt=qs.f_group).order_by('-f_group','f_step').last().f_no
        except:
            # 마지막 게시글 선택시 에러 처리
            qs_next=Fboard.objects.order_by('-f_group','f_step').first().f_no
            
            
    try:
        qs_prev=Fboard.objects.filter(f_group=qs.f_group,f_step__gt=qs.f_step).order_by('-f_group','f_step').first().f_no
    except:
        # 순차적으로 게시글이 등록될때 찾을 수 있는 다음글 검색
        try:
            qs_prev=Fboard.objects.filter(f_group__lt=qs.f_group).order_by('-f_group','f_step').first().f_no
        except:
            # 첫번째 게시글 선택시 에러 처리
            qs_prev=Fboard.objects.order_by('-f_group','f_step').last().f_no
    
    qs.f_hit+=1
    qs.save()
    qsPrev=Fboard.objects.get(f_no=qs_prev)
    qsNext=Fboard.objects.get(f_no=qs_next)
    context={'board':qs,'nowpage':nowpage,'boardPrev':qsPrev,'boardNext':qsNext,'category':category,'searchword':searchword}
    return render(request,'fView.html',context)

# 게시판 글쓰기 함수
def fWrite(request,nowpage,category, searchword):
    if request.method == 'GET':
        context={'nowpage':nowpage,'category':category,'searchword':searchword}
        return render(request,'fWrite.html',context)
    else:
        # form넘어온 데이터
        id = request.POST.get("id")
        member = Member.objects.get(id=id)
        title = request.POST.get("title")
        content = request.POST.get("content")
        file = request.FILES.get("file",None)
        # db 저장
        qs = Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group = qs.f_no
        qs.save()
        return redirect('fboard:fList',nowpage,category,searchword)
        
        

# 게시판 리스트 함수
def fList(request,nowpage,category, searchword):
    # all, title, content
    if request.method=='POST':
        category=request.POST.get('category')
        searchword=request.POST.get('searchword')
        print('POST category : ',category,searchword) # POST로 들어왔을 때 찍힘
        
    print('main category : ',category,searchword) # GET으로 들어왔을 때 찍힘
    # category 분류
    if category == 'first': # GET으로 들어옴.
        qs = Fboard.objects.order_by('-f_group','f_step')
    elif category =='title':
        qs=Fboard.objects.filter(f_title__contains=searchword).order_by('-f_group','f_step')
    elif category == 'content':
        qs=Fboard.objects.filter(f_content__contains=searchword).order_by('-f_group','f_step')
    else: # all
        # # and 검색 : title and content
        # qs=Fboard.objects.filter(f_title__contains=searchword,f_content__contains=searchword)
        # or 검색 : title or content
        qs=Fboard.objects.filter(Q(f_title__contains=searchword)|Q(f_content__contains=searchword)).order_by('-f_group','f_step')


    paginator=Paginator(qs,10) # 1페이지에 나타낼 수 있는 게시글 수 설정
    fList=paginator.get_page(nowpage) # 요청한 페이지의 게시글을 10개 전달
    print('count: ',qs.count)
    context={'fList':fList,'count':qs.count,'nowpage':nowpage,'category':category,'searchword':searchword}
    return render(request,'fList.html',context)
