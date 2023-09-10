from django.shortcuts import render
from .models import contactus
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    data=category.objects.all()
    md={"cdata":data}
    return render(request,'user/index.html',md)
def about(request):
    return render(request,template_name='user/aboutus.html')
def contact(request):
    return render(request,template_name='user/contactus.html')
def signin(request):
    return render(request,template_name='user/signin.html')
def signup(request):
    return render(request,template_name='user/signup.html')
def product(request):
    return render(request,template_name='user/product.html')



def contact(request):
    if request.method=="POST":
      a1=request.POST.get('name')
      a2=request.POST.get('email')
      a3=request.POST.get('mobile')
      a4=request.POST.get('message')
      contactus(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
      return HttpResponse("<script>alert('Thank you for contecting with us');location.href='/user/contact/'</script>")
    return render(request,template_name='user/contactus.html')