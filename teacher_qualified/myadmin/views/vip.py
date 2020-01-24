from django.shortcuts import render

from common.model import Model


def add(request):
    """加载添加页面"""
    return render(request, "myadmin/vip/add.html")


def insert(request):
    """执行添加"""
    if request.POST['no'].replace(' ', '') != '':
        if request.POST['password'] == request.POST['repassword']:
            mod = Model('admin')

            # 获取密码并md5
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'].replace(' ', ''), encoding='utf8'))

            kw = {
                'no': request.POST['no'].replace(' ', ''),
                'password': m.hexdigest(),

            }
            if mod.save(kw) > 0:
                context = {"info": "添加成功！"}
            else:
                context = {"info": "添加失败"}
        else:
            context = {"info": "添加失败"}
    else:
        context = {"info": "添加失败"}
    return render(request, "myadmin/info.html", context)


def edit(request, uid):
    """加载编辑信息页面"""
    mod = Model('admin')
    ob = mod.find(no="'" + uid + "'")
    print(ob)
    if ob is not None:
        context = {"user": ob}
        return render(request, "myadmin/vip/edit.html", context)
    else:
        context = {"info": "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)


def update(request, uid):
    """执行编辑信息"""
    mod = Model('admin')
    ob = mod.find("'"+uid+"'")
    import hashlib
    m = hashlib.md5()
    m.update(bytes(request.POST['old_password'], encoding='utf8'))

    if request.POST['password'] == request.POST['repassword'] and ob[0]['password'] == m.hexdigest():
        mod = Model('admin')
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
    else:
        context = {"info": "修改失败"}
    return render(request, "myadmin/info.html", context)
