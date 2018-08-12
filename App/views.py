import hashlib
import random
import token
import uuid
from time import sleep

import os
from django.core.cache import cache
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import UserModel, BuyerModel
from Day06 import settings


# def index(request):
#     return HttpResponse('Index')


def user_center(request):
    token = request.COOKIES.get('token')
    if not token:
         return render(request,'UserCenter.html')
    try:
        user = UserModel.objects.get(u_token=token)
        username = user.u_name
        return render(request, 'UserCenter.html', context={'username': username})
    except Exception as e:
       return HttpResponse('你已经被强制下线')

def user_register(request):
    if request.method == 'GET':
       return render(request,'UserRegister.html')
    elif request.method == 'POST':
        username = request.POST.get('username')

        user = UserModel()
        user.u_name = username
        token = str(uuid.uuid4())
        user.u_token = token
        user.save()

        return HttpResponse('注册成功%s' % token)


def user_login(request):
    if request.method == 'GET':
        return render(request, 'UserLogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')

        try:
            user = UserModel.objects.get(u_name=username)
            token = user.u_token

            response = HttpResponse('登录成功')
            response.set_cookie('token', token)
            return response
        except Exception as e:
            return redirect(reverse('app:user_login'))

def generate_token(token):
    sha512 = hashlib.sha512()
    sha512.update(token.encode('utf-8'))
    return sha512.hexdigest()

def get_phone(request):

    if random.randrange(100)>90:

        return HttpResponse('恭喜你获得小米256')
    return HttpResponse('正在排队')


def get_ticket(request):
    if random.randrange(100) > 70:
        return HttpResponse('恭喜你抢到满199减188的优惠劵')
    return HttpResponse('下手慢了没有了')
def get_news(request):

    result = cache.get('get_news')

    if result:
        return HttpResponse(result)
    else:
        sleep(3)
        result = '我在这发现了某个同学睡觉了'
        cache.set('get_news', result, timeout=15)
        return HttpResponse(result)


def search(request):
    if request.method == 'GET':
        return render(request, 'search.html')
    elif request.method == 'POST':
        search_field = request.POST.get('searchfield')
        return HttpResponse('帮你查到好多%s有趣的资源' %search_field)


def make_bug(request):

    if random.randrange(10) >5:
        i = 1/0

    return HttpResponse('你最讨厌康熙第几个儿子')


def upload(request):
    if request.method == "GET":
       return render(request, 'Upload.html')
    elif request.method == "POST":
        # print(request.FILES)
        #
        # icon = request.FILES.get('icon')
        # save_file_path = os.path.join(settings.BASE_DIR, 'static/upload/'+str(uuid.uuid4()) +str(icon))
        #
        # with open(save_file_path, 'wb') as save_file:
        #
        #     for part in icon.chunks():
        #         save_file.write(part)
        #         save_file.flush()
        #
        # return HttpResponse('上传成功')
        username = request.POST.get('username')

        icon = request.FILES.get('icon')

        buyer = BuyerModel()
        buyer.b_name = username
        buyer.b_icon = icon
        buyer.save()


        return HttpResponse('上传成功l')