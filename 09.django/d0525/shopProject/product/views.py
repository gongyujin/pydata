from django.shortcuts import redirect, render
from product.models import Product

def pList(request,nowpage):
    qs=Product.objects.order_by('-p_no')
    context={'pList':qs,'nowpage':nowpage}
    return render(request,'pList.html',context)



def pWrite(request,nowpage):
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
        qs=Product(p_category=category,p_name=name,p_servings=serving,p_unitPrice=price,p_description=description,p_manufacturer=manufacturer,p_unit=unit,p_file=file)
        qs.save()        
        return redirect('product:pList',nowpage)

    
    
    