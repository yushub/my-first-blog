from django.shortcuts import HttpResponse  # 导入HttpResponse模块


def index(request):  # request是必须带的实例。类似class下方法必须带self一样
    return HttpResponse("Hello World!!")  # 通过HttpResponse模块直接返回字符串到前端页面
