# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from mypost.models import *

# Create your views here.
def index_view(request,  num='1'):
    page,page_range =Post.get_post_by_page(num,1)
    return render(request,'index.html',context={'page':page,'page_range':page_range})


def post_details_view(request,post_id):
    try:
        posttemp= Post.objects.get(id=post_id)
    except:
        from django.http import Http404,HttpResponse
        raise Http404("你所访问的页面不存在")
    return render(request,'details.html',context={'post':posttemp})


def zhonglei_details_view(request,zhonglei=None):
    post=Post.objects.filter(zhonglei=zhonglei).order_by('-modified').all()

    return render(request,'archive.html',context={'posts':post})


def date_details_view(request,year,month):
    posts= Post.objects.filter(created__year=year,created__month=month).all()

    return render(request,'archive.html',context={'posts':posts})


def search_view(request):
    from haystack.models import SearchResult
    from haystack.query import SearchQuerySet ,SQ
    keywords=request.GET.get('q','')
    # model层也是这样操作的
    from django.core.paginator import Paginator
    pagenitor=Paginator(SearchQuerySet().filter(SQ(title = keywords)|SQ(content = keywords)).all(), 10)
    page = pagenitor.page(1)
    posts = []

    for result in page.object_list:
        posts.append(result.object)
    print  posts
    return render(request,'archive.html',{'posts':posts})