from django.shortcuts import render
from django.http import HttpResponse
import sys
import json
from django.views.decorators.csrf import csrf_exempt

# 导航功能
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

from django.urls import reverse
from django.views.generic import View
import re


# 包的根目录设置
# sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp")
# from models import *

# Create your views here.

class first(View):  # 这里必须要继承View这个类，只有继承了这个url那里的as_view()才会有这个方法
    @csrf_exempt
    def get(self, request,page=None):

        return render(request, 'index.html')

    @csrf_exempt
    def post(self, request):
        return HttpResponse('cbv-post')


def second(request):
    return render(request, 'demo/second.html')


def third(request):
    # a=request.POST['a']
    # b=request.POST['b']
    # outcome=int(a)*int(b)
    test_list = [1, 2, 3, 4, 5, 6, 7]

    return render(request, 'demo/third.html', context={'test_list': test_list})


