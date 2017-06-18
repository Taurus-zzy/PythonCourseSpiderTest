#
# -*- coding: UTF-8 -*-

# #解析器

import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class HtmlParser(object):

    def parse(self, page_url, html_cont):    #定义解析器方法
        if page_url is None or html_cont is None:    #检查被解析的网址和网页文本是否为空
            return
        soup = BeautifulSoup(html_cont, 'html.parser')    #使用BeautifulSoup解析网页文本
        if page_url == 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000':
            new_urls = self.parse_new_urls(page_url, soup)    #只对种子网页进行解析，获取新链接
        else:
            new_urls = set()
        new_data = self.parse_new_data(page_url, soup)    #解析网页，获取所需数据
        return new_urls, new_data

    def parse_new_urls(self, page_url, soup):    #创建方法解析新的待爬取网页
        new_urls = set()
        #解析目录下各个内容的对应超链接：
        #解析超链接所在位置
        links = soup.find('ul', class_='uk-nav uk-nav-side',style="margin-right:-15px;").find_all('a')
        for link in links:            #提取链接
            raw_url = link.get('href')
            new_full_url = urljoin(page_url, raw_url)    #将链接转化为绝对路径形式
            new_urls.add(new_full_url)    #将解析到的链接添加到新链接集合中
        return new_urls


    def parse_new_data(self, page_url, soup):    #创建方法解析出所需数据
        res_data = {}    #创建存储数据的空字典
        res_data['url'] = page_url    #存储第一个值：网址
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('h4').text
        res_data['title'] = title_node
        res_data['content'] = []
        #summary_node = soup.find_all('abc', class_="lemma-summary")
        content_node = soup.find('div', class_="x-wiki-content").find_all('p')
        for txt in content_node:
            res_data['content'].append(txt.text)
        return res_data



