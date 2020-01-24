#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 9:42
# @Author  : 李金哲
# @Site    : 
# @File    : adminmiddleware.py
# @Software: PyCharm
import re

from django.shortcuts import redirect
from django.urls import reverse

class AdminMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Middleware")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # 定义网站后台不用登录也可访问的路由url
        urllist = ['/myadmin/login', '/myadmin/dologin', '/myadmin/logout', '/myadmin/verify',
                   'pc-geetest/ajax_validate', 'pc-geetest/register']
        # 获取当前请求路径
        path = request.path
        print("mycall..." + path)

        # 判断当前请求是否是访问网站后台,并且path不在urllist中
        if re.match("/myadmin", path) and (path not in urllist):
            # 判断当前用户是否没有登录
            if "adminuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('myadmin_login'))

        # 网站前台会员登录判断
        if re.match("^/teacher", path):
            # 判断当前会员是否没有登录
            if "teacher" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('home'))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

