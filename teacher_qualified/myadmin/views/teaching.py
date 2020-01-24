from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

from common.model import Model


# Create your views here.
def index(request):
    """浏览信息"""
    teacher = Model('teacher')
    subject = Model('subject')
    teaching = Model('teaching')
    list1 = teacher.findAll()
    list2 = subject.findAll()
    list3 = teaching.findAll()
    umod = []
    mywhere = []

    for teaching in list3:
        dir = {}
        for subject in list2:
            for teacher in list1:
                if teaching.get('no') == teacher.get('no'):
                    dir.update({'tno': teaching.get('no'), 'tname': teacher.get('name')})
                    break
            if teaching.get('subject') == subject.get('no'):
                dir.update({'sno': subject.get('no'), 'sname': subject.get('name')})
                break
        dir.update({'class': teaching.get('class')})
        umod.append(dir)

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询账户中只要含有关键字的都可以
        list = []
        for vo in umod:
            if vo['tno'].find(kw) >= 0 or vo['tname'].find(kw) >= 0:
                list.append(vo)
        mywhere.append("keyword=" + kw)
    else:
        list = umod

    # 获取、判断并封装学院faculty搜索条件
    subject = request.GET.get('subject', '')
    if subject != '':
        temp = []
        for vo in list:
            if vo['sno'].find(subject) >= 0 or vo['sname'].find(subject) >= 0:
                temp.append(vo)
        mywhere.append("subject=" + subject)
        list = temp

    # 获取、判断并封装教室class搜索条件
    classroom = request.GET.get('class', '')
    if classroom != '':
        temp = []
        for vo in list:
            if vo['class'].find(classroom) >= 0:
                temp.append(vo)
        mywhere.append("class=" + kw)
        list = temp

    # 执行分页处理
    pIndex = int(request.GET.get("p", 1))
    page = Paginator(list, 4)  # 以50条每页创建分页对象
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

    context = {"list": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/teaching/index.html", context)


def add(request):
    """加载添加页面"""
    teacher = Model('teacher')
    subject = Model('subject')
    list1 = teacher.findAll()
    list2 = subject.findAll()

    context = {"teacher": list1, 'subject': list2}
    return render(request, "myadmin/teaching/add.html", context)


def insert(request):
    """执行添加"""
    mod = Model('teaching')
    print(request.POST['teacher'])
    kw = {
        'no': request.POST['teacher'],
        'subject': request.POST['subject'],
        'class': request.POST['class'],
    }
    if mod.save(kw) > 0:
            context = {"info": "添加成功！"}
    else:
        context = {"info": "添加失败"}
    return render(request, "myadmin/info.html", context)


def delete(request, uid):
    """删除信息"""
    mod = Model('teaching')
    if mod.delete(id=uid) > 0:
        context = {"info": "删除成功"}
    else:
        context = {"info": "删除失败"}
    return render(request, "myadmin/info.html", context)


def edit(request, uid):
    """加载编辑信息页面"""
    mod = Model('teaching')
    ob = mod.find(no=uid)

    teacher = Model('teacher')
    subject = Model('subject')
    list1 = teacher.find(no=uid)
    list2 = subject.findAll()

    ob[0].update({'teacher': list1[0].get('name')})
    print(ob)
    print(list2)
    if ob is not None:
        context = {"teaching": ob, 'subject': list2}
        return render(request, "myadmin/teaching/edit.html", context)
    else:
        context = {"info": "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)


def update(request, uid):
    """执行编辑信息"""
    mod = Model('teaching')
    kw = {
        'no': uid,
        'subject': request.POST['subject'],
        'class': request.POST['class'],
    }
    try:
        if mod.update(kw) > 0:
                context = {"info": "修改成功！"}
        else:
            context = {"info": "修改失败"}
    except Exception as err:
        print(err)
        context = {"info": "修改失败"}
    return render(request, "myadmin/info.html", context)
