#
# -*- coding: UTF-8 -*-
class HtmlOutputer(object):

    def __init__(self):    #初始化，得到一个空列表，用于存储数据
        self.datas = []


    def collect_data(self, data):    #创建方法收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):    #创建方法将数据写入"output.txt"。格式为'utf-8'
        fout = open('output.txt', 'w', encoding='UTF-8')
        for data in self.datas:
            fout.write('资料来源：%s \n' % data['url'])
            fout.write('课程名：%s \n' % data['title'])
            fout.write('内容： \n')
            for i in data['content']:
                fout.write(i+ '\n')
            fout.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 课程结束。 \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n\n')
        fout.close()