from django.http import HttpResponse
from django.shortcuts import redirect, render
from freeboard.models import Freeboard

# freeboard fDelete 함수
def fDelete(request,f_no):
    qs=Freeboard.objects.get(f_no=f_no)
    qs.delete()
    
    return redirect('freeboard:fList')

# freeboard fUpdate 함수
def fUpdate(request,f_no):
    if request.method=='GET':
        qs=Freeboard.objects.get(f_no=f_no)
        context={'fboard':qs}
        return render(request,'fUpdate.html',context)
    else:
        qs=Freeboard.objects.get(f_no=f_no)
        qs.f_title=request.POST.get('title')
        qs.f_content=request.POST.get('content')
        qs.save()
        return redirect('freeboard:fList')



    
# freeboard fWrite페에지
def fWrite(request):
    if request.method=='GET':
        return render(request,'fWrite.html')
    else:    
        # f_no
        # f_group=f_no와 같아야함
        # form request데이터를 읽기
        id=request.POST.get('id')
        f_title=request.POST.get('title')
        f_content=request.POST.get('content')
        qs=Freeboard(id=id,f_title=f_title,f_content=f_content)
        qs.save()
        # f_no는 save할때 번호가 생성, AutoField이기 때문에 insert때 생성 -> f_group에 넣음
        qs.f_group=qs.f_no
        qs.save()
        return redirect('freeboard:fList')

# freeboard view페이지
def fView(request,f_no):
    # f_no로 데이터 검색
    qs=Freeboard.objects.get(f_no=f_no)
    context={'fboard':qs}
    return render(request,'fView.html',context)




# freeboard list페이지 함수
def fList(request):
    qs=Freeboard.objects.order_by('-f_no') # f_no로 역순정렬
    context={'fList':qs}
    
    return render(request,'fList.html',context)
    # return HttpResponse('test')