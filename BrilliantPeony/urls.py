"""BrilliantPeony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from  web  import  views
from  django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^favicon.ico',RedirectView.as_view(url=r'/static/images/favicon.ico')),
    re_path('^$', views.index),
    re_path('^about.html$', views.about),
    re_path('^civilization.html$', views.civilization),
    re_path('^news.html$', views.news),
    re_path('^newslist.html$', views.newslist),
    re_path('^news.html$', views.news),
    re_path('^product.html$', views.product),
    re_path('^chuangxin.html$', views.chuangxin),
    re_path('^zeren.html$', views.zeren),
    re_path('^qudao.html$', views.qudao),
    re_path('^contact.html$', views.contact),
    re_path('^company.html$', views.company),
    re_path('^join.html$', views.join),

]
