#!/usr/bin/env python
#coding=utf-8

from django.test import TestCase

# Create your tests here.

from report.models import *


def init():
    # 初始化部门数据
    department_list = []
    zjb_obj = Department(id=1, name="总经办")
    jsb_obj = Department(id=2, name="技术部")
    department_list.append(zjb_obj)
    department_list.append(jsb_obj)
    Department.objects.bulk_create(department_list)

    # 初始化组数据
    other1_obj = Group.objects.create(id=1, name="其他组", department=zjb_obj)
    front_obj = Group.objects.create(id=2, name="前端组", department=jsb_obj)
    develop_obj = Group.objects.create(id=3, name="开发组", department=jsb_obj)
    test_obj = Group.objects.create(id=4, name="测试组", department=jsb_obj)
    design_obj = Group.objects.create(id=5, name="设计组", department=jsb_obj)
    other2_obj = Group.objects.create(id=6, name="其他组", department=jsb_obj)

    # 初始化岗位数据

    Position.objects.create(id=1, name="董事长", group=other1_obj)
    Position.objects.create(id=2, name="总经办主任", group=other1_obj)
    Position.objects.create(id=3, name="法务经理", group=other1_obj)
    Position.objects.create(id=4, name="知识产权专员", group=other1_obj)
    Position.objects.create(id=5, name="其他", group=other1_obj)

    Position.objects.create(id=6, name="技术总监", group=other2_obj)
    Position.objects.create(id=7, name="项目经理", group=other2_obj)
    Position.objects.create(id=8, name="产品", group=other2_obj)
    Position.objects.create(id=9, name="UI设计", group=design_obj)

    Position.objects.create(id=10, name="web前端", group=front_obj)
    Position.objects.create(id=11, name="Android", group=front_obj)
    Position.objects.create(id=12, name="IOS", group=front_obj)

    Position.objects.create(id=13, name="JAVA后台", group=develop_obj)
    Position.objects.create(id=14, name="NET后台", group=develop_obj)

    Position.objects.create(id=15, name="软件测试", group=test_obj)

    Position.objects.create(id=16, name="运维", group=other2_obj)
    Position.objects.create(id=17, name="其他", group=other2_obj)

    # 初始化任务状态表数据
    TaskStatus.objects.create(id=1, name="未开始")
    TaskStatus.objects.create(id=2, name="进行中")
    TaskStatus.objects.create(id=3, name="已完成")
    TaskStatus.objects.create(id=4, name="已暂停")
    TaskStatus.objects.create(id=5, name="已关闭")


def update_userprofile():
    # 根据用户position字段，获取用户的group和department字段并写入userprofile表
    user_objs = User.objects.exclude(username="admin")
    for user in user_objs:
        UserProfile.objects.filter(user=user).update(group=user.userprofile.position.group, department=user.userprofile.position.group.department)
