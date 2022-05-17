from django.shortcuts import render

# 메인페이지
# Create your views here.
def index(request):
    return render(request,'index.html')