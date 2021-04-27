#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   utils.py
@Time    :   2021/4/27 15:00 
@Author  :   Steven Tan
@Version :   1.0
@Contact :   steven.t.y#outlook.com (replace # to @)
@License :   (C)Copyright 2021-2022, Xirui-NLPR-CASIA
@Desc    :   工具类
"""
import json

import requests


class WechatLogin:
    """
    微信登录
    """
    url = "https://api.weixin.qq.com/sns/jscode2session"
    APPID = "*"
    SECRET = "*"

    def __init__(self, code):
        self.code = code

    def login(self):
        payload = {
            'appid': self.APPID,
            'secret': self.SECRET,
            'js_code': self.code,
            'grant_type': 'authorization_code'
        }
        res = requests.get(self.url, params=payload)
        print(res.text)
        return json.loads(res.text)
