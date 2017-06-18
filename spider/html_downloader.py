#
# -*- coding: UTF-8 -*-

# #下载器

import urllib
import requests

class HtmlDownloader(object):

    def download(self, url):  #创建下载器（基于urllib），获取网页文本
        if url is None:
            return None
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()

    def download2(self, url):    #创建下载器（基于requests），获取网页文本
        if url is None:
            return None
        headers = {              #模拟浏览器登陆
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        session=requests.session()                      #建立请求会话
        response = session.get(url, headers=headers)    #获取网页信息

        if response.status_code != 200:    #应对不同的状态码，采用不同的措施
            return None
        return response.text