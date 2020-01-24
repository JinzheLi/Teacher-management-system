from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from common.model import Model


# Create your views here.
def index(request):
    data = request.session['teacher']
    mod = Model('faculty')
    title = mod.findAll()
    for faculty in title:
        if data['faculty'] == faculty['no']:
            data['faculty'] = faculty['name']
    data.pop('password')
    return render(request, "web/teacher/index.html", {'data': data})


def logout(request):
    """执行退出"""
    del request.session['teacher']
    return redirect(reverse('home'))
