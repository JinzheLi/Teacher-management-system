from django.urls import path

from .views import index, users, vip, subject, teaching

urlpatterns = [
    # 后台首页
    path('', index.index, name='myadmin_index'),

    # 后台管理员路由
    path('login', index.login, name="myadmin_login"),
    path('dologin', index.dologin, name="myadmin_dologin"),
    path('logout', index.logout, name="myadmin_logout"),
    # 验证码路由
    path('verify', index.verify, name='myadmin_verify'),

    # 会员信息管理路由
    path('users/', users.index, name='myadmin_users_index'),
    # 添加
    path('users/add', users.add, name='myadmin_users_add'),
    # 执行添加
    path('users/insert', users.insert, name='myadmin_users_insert'),
    # 删除
    path('users/del/<int:uid>/', users.delete, name='myadmin_users_del'),
    # 编辑
    path('users/edit/<int:uid>/', users.edit, name='myadmin_users_edit'),
    # 执行修改
    path('users/update/<int:uid>/', users.update, name='myadmin_users_update'),


    # 管理员路由
    # 添加
    path('vip/add', vip.add, name='myadmin_vip_add'),
    # 执行添加
    path('vip/insert', vip.insert, name='myadmin_vip_insert'),
    # 编辑
    path('vip/edit/<str:uid>/', vip.edit, name='myadmin_vip_edit'),
    # 执行修改
    path('vip/update/<str:uid>/', vip.update, name='myadmin_vip_update'),

    # 课程管理路由
    path('subject/', subject.index, name='myadmin_subject_index'),
    # 添加
    path('subject/add', subject.add, name='myadmin_subject_add'),
    # 执行添加
    path('subject/insert', subject.insert, name='myadmin_subject_insert'),
    # 删除
    path('subject/del/<int:uid>/', subject.delete, name='myadmin_subject_del'),
    # 编辑
    path('subject/edit/<int:uid>/', subject.edit, name='myadmin_subject_edit'),
    # 执行修改
    path('subject/update/<int:uid>/', subject.update, name='myadmin_subject_update'),

    # 课程管理路由
    path('teaching/', teaching.index, name='myadmin_teaching_index'),
    # 添加
    path('teaching/add', teaching.add, name='myadmin_teaching_add'),
    # 执行添加
    path('teaching/insert', teaching.insert, name='myadmin_teaching_insert'),
    # 删除
    path('teaching/del/<int:uid>/', teaching.delete, name='myadmin_teaching_del'),
    # 编辑
    path('teaching/edit/<int:uid>/', teaching.edit, name='myadmin_teaching_edit'),
    # 执行修改
    path('teaching/update/<int:uid>/', teaching.update, name='myadmin_teachering_update'),
]
