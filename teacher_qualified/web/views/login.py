# coding:utf-8
import json

from django.http import HttpResponse
from .geetest import GeetestLib
from common.model import Model
from django.shortcuts import render, redirect
from django.urls import reverse

pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"
mobile_geetest_id = "7c25da6fe21944cfe507d2f9876775a9"
mobile_geetest_key = "f5883f4ee3bd4fa8caec67941de1b903"


def home(request):
    return render(request, "web/login.html")


def pcgetcaptcha(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)

def pcajax_validate(request):
    if request.method == "POST":
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.POST.get('username')
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            teacher = Model('teacher')
            tdata = teacher.find("'" + request.POST.get('username') + "'")
            if tdata:
                import hashlib
                m = hashlib.md5()
                m.update(bytes(request.POST['password'], encoding='utf8'))
                if tdata[0]['password'] == m.hexdigest():
                    # 将当前登陆成功的用户信息以adminuser这个key放入到session中
                    request.session['teacher'] = tdata[0]
                    result = {"status": "success"}
                    # return redirect(reverse('teacher_index'))
                else:
                    result = {"status": "fail"}
            else:
                result = {"status": "fail"}
        else:
            result = {"status": "fail"}
        return HttpResponse(json.dumps(result))
    return HttpResponse("error")
