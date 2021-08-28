from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def greet(request,name):
    #return HttpResponse(f"Hello {name.title()}!")
    return render(request, "hello/greet.html",{
        "name":name.title()
    })

def index(request):
    #return HttpResponse("Hello World!") #这里直接返回了一个字符串的httpresponse
    return render(request,"hello/index.html")

def martin(request):
    return HttpResponse("Hello Martin!")