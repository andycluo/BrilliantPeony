from django.shortcuts import render,HttpResponse
from  web import  models
# Create your views here.

def index(request):
    return  render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def civilization(request):
    return render(request, 'civilization.html')

def news(request):
   news_info  = models.News.objects.filter(nid=2).values('nid','newsimages').first()
   return render(request, 'news.html',{'news_info':news_info})

def product(request):
    return render(request, 'product.html')

def chuangxin(request):
    return render(request, 'chuangxin.html')

def zeren(request):
    return render(request, 'zeren.html')

def qudao(request):
    return render(request, 'qudao.html')

def contact(request):
    return render(request, 'contact.html')

def company(request):
    return render(request, 'company.html')

def join(request):
    return render(request, 'join.html')

def newslist(request):
    return render(request, 'newslist.html')
