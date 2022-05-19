from django.shortcuts import render

def login(request):
    return render(request,'login.html')

def list(request):
    return render(request,'list.html')
