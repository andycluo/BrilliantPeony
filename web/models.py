from django.db import models

# Create your models here.


class home(models.Model):
   """
   主页
   """
   hid = models.BigAutoField(primary_key=True)
   home1 = models.ImageField(max_length=1000, upload_to='static/swf/', verbose_name=u'主页动图', null=True, blank=True)


class about(models.Model):
    """
    关于辉耀
    """
    aid = models.BigAutoField(primary_key=True)
    aboutimage = models.ImageField(max_length=1000, upload_to='static/images/', verbose_name=u'关于动图', null=True, blank=True)

class News(models.Model):
    """
    新闻预览
    """
    nid = models.BigAutoField(primary_key=True)
    newstitle =  models.CharField(verbose_name='新闻标题', max_length=64)
    summary = models.CharField(verbose_name='新闻简介', max_length=64)
    create_time = models.DateTimeField(verbose_name='创建时间',)
    newsimages = models.ImageField(max_length=1000, upload_to='static/imgs/', verbose_name=u'新闻动图', null=True, blank=True)
    content = models.TextField(verbose_name='文章内容', )



class NewsDetail(models.Model):
    """
    新闻详细内容
    """
    content = models.TextField(verbose_name='新闻内容', )

    article = models.OneToOneField(verbose_name='所属文章', on_delete=models.CASCADE, to='News', to_field='nid')
