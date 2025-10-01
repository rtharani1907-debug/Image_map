from django.shortcuts import render
def fun(request):
    return render(request,'map.html')
def com(request):
    return render(request,'company.html')
def far(request):
    return render(request,'farms.html')
def res(request):
    return render(request,'resort.html')
def sch(request):
    return render(request,'school.html')
def wea(request):
    return render(request,'weavers.html')


# Create your views here.
