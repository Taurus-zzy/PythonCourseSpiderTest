# -*- coding: UTF-8 -*-

# 爬虫调度端

from spider import url_manager, html_downloader, html_outputer, html_parser

class SpiderMain(object):

    def __init__(self):  #初始化，
        self.urls = url_manager.UrlManager()                   #创建url管理器实例
        self.downloader = html_downloader.HtmlDownloader()     #创建下载器实例
        self.parser = html_parser.HtmlParser()                 #创建解析器实例
        self.outputer = html_outputer.HtmlOutputer()           #创建数据输出实例

    def craw(self, root_url):  #定义调度方案
        count = 1
        self.urls.add_new_url(root_url)  #将种子网页加入待爬取集合中
        while self.urls.has_new_url():  #判断待爬取集合中是否有未爬取的网页
            try :
                new_url = self.urls.get_new_url()  #取出未爬取的网页
                print('正在爬取第 %d 个网页： %s' % (count, new_url))    #打印正在被爬取网页的地址
                html_cont = self.downloader.download2(new_url)    #获取正在被爬取网页的信息
                new_urls, new_data = self.parser.parse(new_url, html_cont)    #解析网页文本，获取新的网址，获取所需信息
                self.urls.add_new_urls(new_urls)    #将获取新的网址放入待爬取集合中
                self.outputer.collect_data(new_data)    #收集获取到的所需信息
                print('第%d个网页解析完成。'%(count))    #通知解析完成

                if count == 10:        #只解析前20个网页
                    break
                count = count + 1
            except:                                      #异常处理
                count = count + 1
                print('爬取第 %d 个网页时出错' % (count))
        self.outputer.output_html()    #输出所有收集到的信息

if __name__ == "__main__":
    root_url = "http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"  #提供种子网页
    my_spider = SpiderMain()  #创建调度器
    my_spider.craw(root_url)  #运行爬虫方案
