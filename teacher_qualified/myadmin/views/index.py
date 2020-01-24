from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from common.model import Model


# Create your views here.
def index(request):
    """管理后台首页"""
    umod = Model('teacher')
    mode2 = Model('faculty')
    faculty = mode2.findAll()

    list = []
    for vo in faculty:
        dir = {}
        num = umod.count('faculty', vo['no'])[0]['num']
        if num > 0:
            dir.update({'faculty': vo['name'], 'num': num})
            list.append(dir)
    context = {'list': list}

    return render(request, "myadmin/index.html", context)

def login(request):
    """加载登陆页面"""
    return render(request, 'myadmin/login.html')


def dologin(request):
    """执行登陆"""
    # 验证码判断
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info': '验证码错误！'}
        return render(request, "myadmin/login.html", context)

    try:
        # 根据登陆账号获取用户信息
        user = Model('admin')
        user = user.find("'"+request.POST['username']+"'")
        if user is not None:
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding='utf8'))
            print(m.hexdigest())
            # 校验密码是否正确
            if user[0]['password'] == m.hexdigest():
                # 将当前登陆成功的用户信息以adminuser这个key放入到session中
                request.session['adminuser'] = user[0]
                return redirect(reverse('myadmin_index'))
            else:
                context = {'info': "登陆密码错误"}
        else:
            context = {'info': "此用户非后台管理账户"}
    except Exception as err:
        print(err)
        context = {'info': "登陆账号不存在"}
    return render(request, 'myadmin/login.html', context)


def logout(request):
    """执行退出"""
    del request.session['adminuser']
    return redirect(reverse('myadmin_login'))


def verify(request):
    # 引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    # 定义变量，用于画面的背景色、宽、高
    # bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242, 164, 247)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    # str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/msyh.ttf', 21)
    # font = ImageFont.load_default().font
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

