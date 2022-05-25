from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F
from django.core.paginator import Paginator

def fReply(request,f_no,nowpage):
    if request.method=='GET':
        qs=Fboard.objects.get(f_no=f_no)
        context={'board':qs,'nowpage':nowpage}
        return render(request,'fReply.html',context)
    else:
        id=request.POST.get('id')
        member=Member.objects.get(id=id)
        
        group=int(request.POST.get('group'))
        indent=int(request.POST.get('indent'))
        step=int(request.POST.get('step'))
        
        title=request.POST.get('title')
        content=request.POST.get('content')
        file=request.FILES.get('file',None)
        
        Fboard.objects.filter(f_group=group,f_step__gt=step).update(f_step=F('f_step')+1)
        
        qs=Fboard(member=member,f_title=title,f_content=content,f_file=file,\
        f_group=group,f_step=step+1,f_indent=indent+1)
        qs.save()
        return redirect('fboard:fList',nowpage)

def fUpdate(request,f_no,nowpage):
    if request.method=='GET':
        qs=Fboard.objects.get(f_no=f_no)
        context={'board':qs,'nowpage':nowpage}
        return render(request,'fUpdate.html',context)
    else:
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        title=request.POST.get('title')
        content=request.POST.get('content')
        file=request.FILES.get('file',None)
        
        qs=Fboard.objects.get(f_no=f_no)
        qs.f_title=title
        qs.f_content=content

        if file:
            qs.f_file=file
        
        qs.save()
        return redirect('fboard:fList',nowpage)


def fDelete(request,f_no,nowpage):
    qs=Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage)


def fList(request,nowpage):
    qs=Fboard.objects.order_by('-f_group','f_step')
    
    paginator=Paginator(qs,10)
    fList=paginator.get_page(nowpage)
    context={'fList':fList,'nowpage':nowpage}
    return render(request,'fList.html',context)

def fWrite(request,nowpage):
    if request.method=='GET':
        context={'nowpage':nowpage}
        return render(request,'fWrite.html',context)
    else:
        id=request.POST.get('id')
        member=Member.objects.get(id=id)
        title=request.POST.get('title')
        content=request.POST.get('content')
        file=request.FILES.get('file',None)
        
        qs=Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group=qs.f_no
        qs.save()
        return redirect('fboard:fList',nowpage)
        

def fView(request,f_no,nowpage):
    qs=Fboard.objects.get(f_no=f_no)
    qs.f_hit+=1
    qs.save()
    context={'board':qs,'nowpage':nowpage}
    return render(request,'fView.html',context)
