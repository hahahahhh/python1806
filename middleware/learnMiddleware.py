import random

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django_redis import cache


class HelloMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # print('Hello')
        # print(request.path, request.META.get('REMOTE_ADDR'))
        if request.path == '/app/getphone/':
            if request.META.get('REMOTE_ADDR') == '10.0.118.85':
                r = random.randrange(10)
                if r > 5:
                    return HttpResponse('恭喜你抢到小米256')
                elif r > 2:
                    return HttpResponse('恭喜你抢到小米256')
                else:
                    return HttpResponse('正在排队')
            elif request.path == '/app/getticket/':
                if request.META.get('REMOTE ADDR') == '10.0.118.85':
                    return HttpResponse('下手慢了,没有了')
            elif request.path == '/app/search/':
                if request.method == 'POST':

                    result = cache.get(request.META.get('REMDTE_ADDR'))
                    if result:
                        return HttpResponse('小爬虫,不要爬了,我这没什么好玩的')
                    else:
                        cache.set(request.META.get('REMOTE_ADDR'), '这有好玩东西', timeout=15),

    def process_exception(self, request, exception):
        print(str(exception))
        return redirect(reverse('app:index'))

