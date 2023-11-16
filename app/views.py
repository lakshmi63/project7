from django.shortcuts import render

# Create your views here.
def login(request):
    data='vara'
    d={'name':data}
    return render(request,'login.html',context=d)