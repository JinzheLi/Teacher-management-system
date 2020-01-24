from django.shortcuts import render
from django.core.paginator import Paginator

from common.model import Model


# Create your views here.
def index(request):
    """浏览信息"""
    # sql ='select teacher.no,teacher.faculty,teacher.name,teacher.age,teacher.' \
    #      'sex,teacher.position,teacher.degree,phone,faculty.name fa_name from teacher, ' \
    #      'faculty where teacher.faculty=faculty.no'
    teacher = Model('teacher')
    mode2 = Model('faculty')

    list1 = teacher.findAll()
    faculty = mode2.findAll()

    umod = []
    mywhere = []
    sss = {'name': 1}
    # 1、消除教师的密码信息，2、把教师中的学院no更新为学院name
    for teaching in list1:
        dir = {}
        for vo in faculty:
            if teaching.get('faculty') == vo.get('no'):
                dir.update({'no': teaching.get('no'), 'name': teaching.get('name'), 'fa_name': vo.get('name'),
                            'sex': teaching.get('sex'), 'age': teaching.get('age'),
                            'position': teaching.get('position'),
                            'degree': teaching.get('degree'), 'phone': teaching.get('phone')})
                break
        umod.append(dir)

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

    # 获取、判断并封装学院faculty搜索条件
    facu = request.GET.get('faculty', '')
    if facu != '':
        temp = []
        for vo in list:
            if vo['fa_name'] == facu:
                temp.append(vo)
        mywhere.append("faculty=" + facu)
        list = temp

    # 获取、判断并封装职位faculty搜索条件
    position = request.GET.get('position', '')
    if position != '':
        temp = []
        for vo in list:
            if vo['position'] == position:
                temp.append(vo)
        mywhere.append("position=" + position)
        list = temp

    # 获取、判断并封装学历degree搜索条件
    degree = request.GET.get('degree', '')
    if degree != '':
        temp = []
        for vo in list:
            if vo['degree'] == degree:
                temp.append(vo)
        mywhere.append("degree=" + degree)
        list = temp

    # 执行分页处理
    pIndex = int(request.GET.get("p", 1))
    page = Paginator(list, 4)  # 以4条每页创建分页对象
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

    context = {"userslist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'faculty': faculty,
               'mywhere': mywhere}
    return render(request, "myadmin/users/index.html", context)


def add(request):
    """加载添加页面"""
    mod = Model('faculty')
    title = mod.findAll()
    context = {'typelist': title}
    return render(request, "myadmin/users/add.html", context)


def insert(request):
    """执行添加"""
    mod = Model('teacher')

    # 获取密码并md5
    import hashlib
    m = hashlib.md5(b'000000')

    try:
        kw = {
            'no': request.POST['no'].strip(),
            'faculty': request.POST['faculty'],
            'name': request.POST['name'],
            'age': request.POST['age'],
            'sex': request.POST['sex'],
            'position': request.POST['position'],
            'degree': request.POST['degree'],
            'phone': request.POST['phone'],
            'password': m.hexdigest(),
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
    mod = Model('teacher')
    if mod.delete(id=uid) > 0:
        context = {"info": "删除成功"}
    else:
        context = {"info": "删除失败"}
    return render(request, "myadmin/info.html", context)


def edit(request, uid):
    """加载编辑信息页面"""
    mod = Model('teacher')
    ob = mod.find(no=uid)
    mod = Model('faculty')
    title = mod.findAll()
    if ob is not None:
        context = {"user": ob, 'typelist': title}
        return render(request, "myadmin/users/edit.html", context)
    else:
        context = {"info": "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)


def update(request, uid):
    """执行编辑信息"""
    if request.POST['password'] == request.POST['repassword']:
        mod = Model('teacher')

        # 获取密码并md5
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding='utf8'))

        kw = {
            'no': uid,
            'faculty': request.POST['faculty'],
            'age': request.POST['age'],
            'sex': request.POST['sex'],
            'position': request.POST['position'],
            'degree': request.POST['degree'],
            'phone': request.POST['phone'],
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
