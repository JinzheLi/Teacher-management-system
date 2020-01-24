from django.shortcuts import render
from django.core.paginator import Paginator

from common.model import Model


# Create your views here.
def index(request):
    """浏览信息"""
    mod = Model('subject')
    umod = mod.findAll()
    mywhere = []

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询账户中只要含有关键字的都可以
        list = []
        for vo in umod:
            if vo['no'].find(kw) >= 0 or vo['name'].find(kw) >= 0:
                list.append(vo)
        mywhere.append("keyword=" + kw)
    else:
        list = umod

    # 获取、判断并封装学分score搜索条件
    score = request.GET.get('score', '')
    if score != '':
        temp = []
        for vo in list:
            if vo['score'] == float(score):
                temp.append(vo)
        mywhere.append("score=" + kw)
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
    return render(request, "myadmin/subject/index.html", context)


def add(request):
    """加载添加页面"""
    return render(request, "myadmin/subject/add.html")


def insert(request):
    """执行添加"""
    mod = Model('subject')
    try:
        kw = {
            'no': request.POST['no'],
            'name': request.POST['name'],
            'score': request.POST['score'],
        }
        if mod.save(kw) > 0:
                context = {"info": "添加成功！"}
        else:
            context = {"info": "添加失败"}
    except:
            context = {"info": "添加失败"}
    return render(request, "myadmin/info.html", context)


def delete(request, uid):
    """删除信息"""
    mod = Model('subject')
    if mod.delete(id=uid) > 0:
        context = {"info": "删除成功"}
    else:
        context = {"info": "删除失败"}
    return render(request, "myadmin/info.html", context)


def edit(request, uid):
    """加载编辑信息页面"""
    mod = Model('subject')
    ob = mod.find(no=uid)
    if ob is not None:
        context = {"user": ob}
        return render(request, "myadmin/subject/edit.html", context)
    else:
        context = {"info": "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)


def update(request, uid):
    """执行编辑信息"""
    mod = Model('subject')
    kw = {
        'no': uid,
        'name': request.POST['name'],
        'score': request.POST['score'],
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
