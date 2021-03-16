#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "martin"

import json
import datetime
import random

from django.http import HttpResponse
from django.shortcuts import redirect

import xlwt


class JSONResponse(HttpResponse):
    """JSON response class."""

    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = json.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)


def login_required_by_render(func):
    def wrapped_fuc(request, *args, **kwargs):
        user = request.request.user

        if not user.is_authenticated:
            return redirect('/report/login')
        else:
            return func(request, *args, **kwargs)

    return wrapped_fuc


def login_required_by_ajax(func):
    def wrapped_fuc(request, *args, **kwargs):
        user = request.request.user

        if not user.is_authenticated:
            return JSONResponse({'code': 1, 'error': '当前未登录'})
        else:
            return func(request, *args, **kwargs)

    return wrapped_fuc


def is_superuser(func):
    def wrapped_fuc(request, *args, **kwargs):
        user = request.request.user

        if not user.is_authenticated or not user.is_superuser:
            return JSONResponse({'code': 2, 'error': '抱歉，你不是超级管理员！'})
        else:
            return func(request, *args, **kwargs)

    return wrapped_fuc


def get_this_monday():
    today = datetime.date.today()
    weekday = today.weekday()
    return today-datetime.timedelta(weekday)


def generate_verification_code(len=6):
    """
    随机生成6位数字验证码
    :param len:
    :return:
    """
    num_list = []
    for i in range(9):
        num_list.append(str(i))
    code_list = random.sample(num_list, 6)
    verification_code = ''.join(code_list)
    return verification_code


def excel_head_style():
    """
        定义导出文件表头格式
    :return:
    """
    # 创建一个样式
    style = xlwt.XFStyle()
    # 设置背景色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    # 设置单元格背景色
    pattern.pattern_fore_colour = xlwt.Style.colour_map['light_green']
    style.pattern = pattern
    # 设置字体
    font0 = xlwt.Font()
    font0.name = u'宋体'
    font0.bold = True
    font0.colour_index = 0
    font0.height = 240
    style.font = font0
    # 设置文字位置
    alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
    style.alignment = alignment
    # 设置边框
    borders = xlwt.Borders()  # Create borders
    borders.left = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.right = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.top = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.bottom = xlwt.Borders.THIN  # 添加边框-虚线边框
    style.borders = borders

    return style


def excel_record_style():
    """
        定义导出文件记录格式
    :return:
    """
    # 创建一个样式
    style = xlwt.XFStyle()
    # 设置字体
    font0 = xlwt.Font()
    font0.name = u'微软雅黑'
    font0.bold = False
    font0.colour_index = 0
    font0.height = 240
    style.font = font0
    # 设置文字位置
    alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    # alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    alignment.horz = xlwt.Alignment.HORZ_LEFT  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
    style.alignment = alignment
    # 设置边框
    borders = xlwt.Borders()  # Create borders
    borders.left = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.right = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.top = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.bottom = xlwt.Borders.THIN  # 添加边框-虚线边框
    style.borders = borders

    return style


def wite_to_excel(wbk_obj, sheet_name, head_data, records, download_url, report_obj, department_name):
    """
        写入excel文件函数
    :param n: 数据有多少行
    :param sheet_name：工作表名字，这里有三个，本周、下周和遗留
    :param head_data: 表头列表
    :param records: 表格数据，所有数据是一个列表，里面的每一行是一个列表，例如：[[123, 456], [123, 456], [123, 456],]
    :param download_url: 下载url
    :return:
    """
    data_row = len(records)

    # 获取字符串长度，一个中文的长度为2
    def len_byte(value):
        value = str(value)
        length = len(value)
        utf8_length = len(value.encode('utf-8'))
        length = (utf8_length - length) / 2 + length
        return int(length)

    sheet_obj = wbk_obj.add_sheet(sheet_name, cell_overwrite_ok=True)

    # 写入表头
    head_style_obj = excel_head_style()
    # 设置行高
    tall_style = xlwt.easyxf('font:height 480')  # 24pt
    sheet_obj.row(0).set_style(tall_style)
    for filed in range(0, len(head_data)):
        sheet_obj.write(0, filed, head_data[filed], head_style_obj)

    # 写入数据记录
    record_style_obj = excel_record_style()
    for row in range(1, data_row+1):
        # 设置行高
        tall_style = xlwt.easyxf('font:height 480')  # 24pt
        sheet_obj.row(row).set_style(tall_style)
        for col in range(0, len(head_data)):
            sheet_obj.write(row, col, records[row-1][col], record_style_obj)

    col_width = {}
    for i in range(len(head_data)):
        col_width[i] = len_byte(head_data[i])
        for j in range(data_row):
            if len_byte(records[j][i]) > col_width[i]:
                col_width[i] = len_byte(records[j][i])

    # 设置栏位宽度
    for i in range(len(head_data)):
        try:
            sheet_obj.col(i).width = 256 * (col_width[i] + 8)
        except ValueError as e:
            sheet_obj.col(i).width = 256 * 255

    # wbk_obj.save("%s技术部-%s年第%s周周报统计表.xls" % (download_url, report_obj.year, report_obj.weekly_num))
    wbk_obj.save("%s/%s-%s年第%s周周报统计表.xls" % (download_url, department_name, report_obj.year, report_obj.weekly_num))
    return "ok"