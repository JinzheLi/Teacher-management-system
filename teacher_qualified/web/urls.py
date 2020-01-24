from django.urls import path

from .views import index
from django.conf.urls import url

from .views import login, teacher

urlpatterns = [
    path('pc-geetest/register', login.pcgetcaptcha, name='pcgetcaptcha'),
    path('pc-geetest/ajax_validate', login.pcajax_validate, name='pcajax_validate'),
    path('', login.home, name='home'),
    path('logout', index.logout, name="teacher_logout"),

    # 前台首页
    path('teacher/', index.index, name="teacher_index"),
    # 编辑
    path('teacher/edit/<int:uid>/', teacher.edit, name='teacher_edit'),
    # 执行修改
    path('teacher/update/<int:uid>/', teacher.update, name='teacher_update'),
    path('teacher/teaching/', teacher.teaching, name='teacher_teaching'),
]

# urlpatterns = [
#     path('login/', index.login, name="login"),
# ]
