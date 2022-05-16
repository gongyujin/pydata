from django.shortcuts import render

# Create your views here.
def boardList(request):
    return render(request,'boardList.html')