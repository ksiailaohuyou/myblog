# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Zhonglei(models.Model):
    name=models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return u'%s'%self.name

class Biaoqian(models.Model):
    name=models.CharField(max_length=20 ,unique=True)
    def __unicode__(self):
        return u'%s'%self.name

class Post(models.Model):
    title=models.CharField(max_length=20,verbose_name='题目')
    decs =RichTextUploadingField(verbose_name='描述')
    content=models.TextField(verbose_name='描述',null=True,blank=True,default='非必须项')
    created=models.DateField(auto_now_add=True,verbose_name='创建时间')
    modified=models.DateField(auto_now=True,verbose_name='修改')
    zhonglei=models.ForeignKey(Zhonglei,verbose_name='种类')
    biaoqian=models.ManyToManyField(Biaoqian,verbose_name='标签')
    @staticmethod
    def get_post_by_page(num,per_page=1):#num 第几页  per_page  没有有多少个
        num=int(num)
        from django.core.paginator import Paginator
        fenye=Paginator(Post.objects.order_by('-modified').all(),per_page)
        if num<1:
            num = 1
        if num>fenye.num_pages:#num_pages总的页数
            num = fenye.num_pages
        page = fenye.page(num)

        pervious = 2
        last = 2
        if num <= pervious:
            start = 1
            end = last + pervious + 1
        if num > pervious:
            start = num - pervious + 1
            end = num + last + 1
        if end > fenye.num_pages:
            min = end - fenye.num_pages
            end = fenye.num_pages
            start -= min
            if start <= 1:
                start = 1
        # pagintor.page_range
        return (page, range(start, end + 1))




