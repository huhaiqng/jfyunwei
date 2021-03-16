#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "martin"

import requests
import json
from jsb.settings import api_url_jsb, api_url_zjb

headers = {'Content-Type': 'application/json'}


def msg(user, text, api_url=api_url_jsb):

    json_text = {
        "msgtype": "text",
        "text": {
            "content": "@%s, %s" % (user, text)
        },
        "at": {
            "atMobiles": [
                user
            ],
            "isAtAll": False
        }
    }
    requests.post(api_url, data=json.dumps(json_text), headers=headers).json()


def msg_link(title, text, api_url=api_url_jsb):

    json_text = {
        "msgtype": "link",
        "link": {
            "title": title,
            "text": text,
            # "picUrl": "http://192.168.40.159/static/version/img/jpark.png",
            # "messageUrl": "http://192.168.40.159"
            "picUrl": "http://jf.zhubaogongyuan.cn:888/static/version/img/jpark.png",
            "messageUrl": "http://jf.zhubaogongyuan.cn:888"
        },
        "at": {
            "atMobiles": [
                ''
            ],
            "isAtAll": True
        }
    }
    requests.post(api_url, data=json.dumps(json_text), headers=headers).json()


def version_msg(user, text, title, api_url=api_url_jsb):
    json_text = {
        "msgtype": "link",
        "link": {
            "title": title,
            "text": text,
            "picUrl": "http://192.168.40.159/static/version/img/jpark.png",
            "messageUrl": "http://192.168.40.159/version/"
        },
        "at": {
            "atMobiles": [
                user
            ],
            "isAtAll": True
        }
    }
    requests.post(api_url, data=json.dumps(json_text), headers=headers).json()
