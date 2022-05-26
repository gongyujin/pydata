from django.shortcuts import render,redirect
from product.models import Product
from django.db.models import F

# 상품등록 수정페이지 함수
def pUpdate(request,p_no):
    if request.method=='GET':
        qs=Product.objects.get(p_no=p_no)
        context={'product':qs}
        return render(request,'pUpdate.html',context)
    else:
        category =request.POST.get('category')
        name =request.POST.get('name')
        serving =request.POST.get('serving')
        price =request.POST.get('price')
        description =request.POST.get('description')
        manufacturer =request.POST.get('manufacturer')
        unit =request.POST.get('unit')
        file =request.FILES.get('file',None)
        
        # db저장
        qs=Product.objects.get(p_no=p_no)
        qs.p_category=category
        qs.p_name=name
        qs.p_servings=serving
        qs.p_unitPrice=price
        qs.p_description=description
        qs.p_manufacturer=manufacturer
        qs.p_unit=unit
        if file:
            qs.p_fileName=file
            
        qs.save()        
        return redirect('product:pList')



# 상품등록페이지 함수
def pWrite(request):
    if request.method=='GET':
        return render(request,'pWrite.html')
    else:
        category =request.POST.get('category')
        name =request.POST.get('name')
        serving =request.POST.get('serving')
        price =request.POST.get('price')
        description =request.POST.get('description')
        manufacturer =request.POST.get('manufacturer')
        unit =request.POST.get('unit')
        file =request.FILES.get('file',None)
        
        # db저장
        qs=Product(p_category=category,p_name=name,p_servings=serving,p_unitPrice=price,p_description=description,p_manufacturer=manufacturer,p_unit=unit,p_fileName=file)
        qs.save()        
        return redirect('product:pList')


# 상품리스트 페이지 함수
def pList(request):
    qs=Product.objects.order_by('-p_no')
    context={'pList':qs}
    return render(request,'pList.html',context)