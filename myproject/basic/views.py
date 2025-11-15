from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('welcome to django')
    
def sampleInfo(request):
    # data={"name":'Nikitha','age':22,'city':'hyd'}
    data={'result':[4,6,8,9]}
    return JsonResponse(data)

def dynamicResponse(request):
    name=request.GET.get("name",'lychuu')
    city=request.GET.get("city",'nzd')

    return HttpResponse(f"hello {name} from {city}")