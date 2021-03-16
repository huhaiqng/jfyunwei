#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "martin"

import json
from django.http import HttpResponse


class JSONResponse(HttpResponse):
    """JSON response class."""

    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = json.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)


def login_required_by_ajax(func):
    def wrapped_fuc(request, *args, **kwargs):
        user = request.request.user

        if not user.is_authenticated:
            return JSONResponse({'code': -1, 'msg': '请点击右上角进行登录！'})
        else:
            return func(request, *args, **kwargs)

    return wrapped_fuc


def is_superuser(func):
    def wrapped_fuc(request, *args, **kwargs):
        user = request.request.user

        if not user.is_authenticated or not user.is_superuser:
            return JSONResponse('You are not superuser!')
        else:
            return func(request, *args, **kwargs)

    return wrapped_fuc





