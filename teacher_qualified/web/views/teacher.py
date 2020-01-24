from django.shortcuts import render
from django.core.paginator import Paginator

from common.model import Model


def edit(request, uid):
    """加载编辑信息页面"""
    mod = Model('teacher')
    ob = mod.find("'" + str(uid) + "'")
    if ob is not None:
        context = {"teacher": ob}
        return render(request, "web/teacher/edit.html", context)
    else:
        context = {"info": "没有找到要修改的信息！"}
        return render(request, "web/info.html", context)


def update(request, uid):
    """执行编辑信息"""
    mod = Model('teacher')
    uid = str(uid)
    ob = mod.find("'" + uid + "'")
    if request.POST['old_password'] == '':
        context = {"info": "请输入登录密码"}
        return render(request, "web/info.html", context)
    else:
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['old_password'], encoding='utf8'))
    if ob[0]['password'] == m.hexdigest():
        if request.POST['password'] != '' and request.POST['password'] == request.POST['repassword']:
            mod = Model('teacher')
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding='utf8'))
            kw = {
                'no': uid,
                'password': m.hexdigest(),
            }
            try:
                if mod.update(kw) > 0:
                    context = {"info": "修改成功！"}
                else:
                    context = {"info": "修改失败"}
            except Exception as err:
                print(err)
                context = {"info": "修改失败"}
        elif request.POST['password'] == '' and request.POST['phone'] != '':
            kw = {
                'no': uid,
                'phone': request.POST['phone'],
            }
            try:
                if mod.update(kw) > 0:
                    context = {"info": "修改成功！"}
                else:
                    context = {"info": "修改失败"}
            except Exception as err:
                print(err)
                context = {"info": "修改失败"}
        else:
            context = {"info": "无修改信息"}
    else:
        context = {"info": "修改失败"}
    return render(request, "web/info.html", context)


def teaching(request):
    """课程安排"""
    data = request.session['teacher']
    uid = data.get('no')
    subject = Model('subject')
    teaching = Model('teaching')
    list2 = subject.findAll()
    list3 = teaching.find("'" + uid + "'")
    umod = []

    for teaching in list3:
        dir = {}
        for subject in list2:
            if teaching.get('subject') == subject.get('no'):
                dir.update({'no': subject.get('no'), 'name': subject.get('name'), 'score': subject.get('score')})
                break
        dir.update({'class': teaching.get('class')})
        umod.append(dir)

    # 执行分页处理
    pIndex = int(request.GET.get("p", 1))
    page = Paginator(umod, 4)  # 以50条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    # 获取页面列表信息
    if maxpages < 5:
        plist = page.page_range  # 页码数列表
    else:
        if pIndex <= 3:
            plist = range(1, 6)
        elif pIndex >= maxpages - 3:
            plist = range(maxpages - 4, maxpages + 1)
        else:
            plist = range(pIndex - 2, pIndex + 3)

    context = {"list": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages}
    return render(request, "web/teacher/class.html", context)
