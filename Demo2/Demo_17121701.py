# -*- coding: utf-8 -*-
import os
import os.path
# import sys
#
# reload(sys)
import importlib
# import sys
import urllib.request

from bs4 import BeautifulSoup

# importlib.reload(sys)

# sys.setdefaultencoding("utf-8")  # 开奖日期中的字符需要引入
# import urllib2




# 创建/打开一个文件放数据
def fetchLottery():
    print(os.path)
    if os.path.exists("lottery.csv"):
        os.remove("lottery.csv")
    f = open("lottery.csv", "a")
    for i in range(3, 16):
        print("正在获取" + "{:0>2d}".format(i) + "年数据")
        # url = "http://www.lecai.com/lottery/draw/list/50?type=range_date&start=20" + "{:0>2d}".format(
        #     i) + "-01-01&end=20" + "{:0>2d}".format(i) + "-12-31"
        url = "http://zst.aicai.com/ssq/openInfo/"
        print("url:"+url)
        page = urllib.request.urlopen(url)  # 打开目标url
        soup = BeautifulSoup(page, "html.parser")  # 格式化标签
        # print(soup.find_all(attrs={"class":"historylist"}))
        # foundAllTbody = soup.findAll(attrs={"class": "balls"})
        foundAllTbody = soup.findAll(attrs={"class": "camBlue"})
        foundDate = soup.findAll("tbody")[0]
        num = 1
        if (foundAllTbody):
            for foundBalls in foundAllTbody[0:]:
                # foundAllTd = foundBalls.findAll("td")
                # if(foundAllTd):
                #     for foundTd1 =
                # foundAllTr = foundBalls.findAll("em")
                foundAllTd = foundBalls.findAll("td")
                if (foundAllTd):
                    ballStr = ""
                    for foundTd in foundAllTd[2:9]:
                        if (foundTd):
                            ballStr += ","
                            ballStr += foundTd.string
                    for foundTd1 in foundAllTd[1:2]:
                        if (foundTd1):
                            date = foundTd1.string
                            # print(foundTd.string)
                # date = foundDate.findAll("td")[(num - 1) * 10 + num].string  # 开奖日期
                # date = "20171217"
                print(type(date))
                f.write(date + ',' + ballStr + '\n')
                # print(foundDate.findAll("td")[(num - 1) * 10 + num].string)
                num = num + 1
    print("数据抓取完成")
    f.close()


fetchLottery()
