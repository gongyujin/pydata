from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    ## HttpResonse : data 형태로 전달
    # return HttpResponseRedirect('<h2>여기에 글자를 페이지에 리턴해줌.</h2>')