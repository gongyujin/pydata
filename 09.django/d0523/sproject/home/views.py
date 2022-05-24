from django.shortcuts import render
from product.models import Product
def index(request):
   qs=Product.objects.order_by('p_no')
   context={'pList':qs}
   return render(request,'index.html',context) 
