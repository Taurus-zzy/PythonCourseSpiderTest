#
# -*- coding: UTF-8 -*-

#URL管理器

class UrlManager(object):
    def __init__(self):   #创建两个空集合用于存储待爬取的网站和已经爬取的网站
        self.new_urls = set()  #待爬取的网页集合
        self.old_urls = set()  #已爬取的网页集合

    def add_new_url(self, url):  #创建方法，将一个新的网页加入到待爬取的网页集合
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):  #创建方法，将新的网页加入到待爬取的网页集合
        if len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  #创建方法，判断待爬取的网页集合是否有未爬取的网页
        return len(self.new_urls) != 0


    def get_new_url(self):  #创建方法，从待爬取的网页集合中提取一个网页，并将其至放入已爬取集合中
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url



