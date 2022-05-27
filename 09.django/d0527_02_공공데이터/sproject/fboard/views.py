from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F,Q
from django.core.paginator import Paginator
import requests
import json

# 이벤트
def event(request):
    return render(request,'event.html')

# 이벤트 뷰페이지
def event_view(request):
    return render(request,'event_view.html')



# 코로나 공공데이터
def c_list(request):
    public_key='Ipx52TKNQYQIqd8pC9w%2BMQqG5uX8b%2FLcUqiDf3jra%2BLewkrmtRm4dHzr9DCkzX8fyXhP3hJZnDtt%2BDst718ZMg%3D%3D'
    url='https://api.odcloud.kr/api/15077756/v1/vaccine-stat?page=1&perPage=10&serviceKey={}'.format(public_key)
    res=requests.get(url)
    json_res=json.loads(res.text)
    raw_data=json_res['data']
    context={'data_list':raw_data}
    return render(request,'c_list.html',context)


# 공공데이터 검색
def data_search(request):
    # 검색부분에 빙수라는 단어를 입력하고 검색버튼을 클릭을 하면
    # 빙수 리스트가 출력될 수 있도록 구성하시오.
    keyword=request.POST.get('searchword')
    print(keyword)
    print("-"*50)
    # qs=Fboard.objects.filter(Q(f_title__contains=searchword)|Q(f_content__contains=searchword)).order_by('-f_group','f_step')

    public_key='Ipx52TKNQYQIqd8pC9w%2BMQqG5uX8b%2FLcUqiDf3jra%2BLewkrmtRm4dHzr9DCkzX8fyXhP3hJZnDtt%2BDst718ZMg%3D%3D'
    # # 갤러리 목록조회
    # url='http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList?&serviceKey={}&pageNo={}&numOfRow=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&title={}&_type=json'.format(public_key,page,keyword)
    # 갤러리검색조회
    url='http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/gallerySearchList?&serviceKey={}&pageNo=1&numOfRow=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&keyword={}&_type=json'.format(public_key,keyword)
    # 웹스크래핑
    res=requests.get(url) # str 타입
    # json타입
    json_res=json.loads(res.text) # json타입으로 변경
    dList=json_res['response']['body']['items']['item']
    # print(dList)
    context={'dList':dList}
    return render(request,'data_list.html',context)


# 공공데이터 함수
def data_list(request):
    page=request.GET.get('page')
    if not page:
        page=1
    # keyword='빙수'
    public_key='Ipx52TKNQYQIqd8pC9w%2BMQqG5uX8b%2FLcUqiDf3jra%2BLewkrmtRm4dHzr9DCkzX8fyXhP3hJZnDtt%2BDst718ZMg%3D%3D'
    # # 갤러리 목록조회
    url='http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList?&serviceKey={}&pageNo={}&numOfRow=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'.format(public_key,page)
    # 갤러리검색조회
    # url='http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/gallerySearchList?&serviceKey={}&pageNo={}&numOfRow=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&keyword={}&_type=json'.format(public_key,page,keyword)
    # 웹스크래핑
    res=requests.get(url) # str 타입
    # json타입
    json_res=json.loads(res.text) # json타입으로 변경
    dList=json_res['response']['body']['items']['item']
    # print(dList)
    context={'dList':dList}
    return render(request, 'data_list.html',context)


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
