from  mypost.models import *
from  datetime import *
from django.db.models import *


def slider_context(request):
    context={}
    context['category']=Post.objects.values('zhonglei','zhonglei__name').annotate(count = Count('*'))

    archive = Post.objects.values('created').order_by('-created')
    context['archive']=archive
    context['recent']=Post.objects.order_by('-created').all()[:5]
    return context