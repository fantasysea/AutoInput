# -*- coding:utf-8 -*-

import os;
import re
import requests
import json
def getTitle():
    for i in range(1, 10, 1):
        #perfume box res = requests.get("https://www.alibaba.com/products/F0/perfume_box/--CN----------------------------10-350333--------------------------------------------------------CNTRY-CN,ATTR-10-350333/"+str(i)+".html")
        res = requests.get("https://www.alibaba.com/products/F0/jewelry_box/------------------------------217-352685/"+str(i)+".html")
        # print res.text
        pattern = re.compile(r"_search_result_data = ([\s\S]*) page.setPageData", re.M|re.I)
        #pattern = re.compile(r"<span .* Follow Us:</span>", re.M|re.I)
        match = pattern.search(res.text)#一定要用search啊!match是全部匹配
        if match:
            # 使用Match获得分组信息
            # print match.group(1)
            data = json.loads(match.group(1))
            # print data['normalList']
            for product in data['normalList']:
                if len(product["productPuretitle"])>60:
                    print product["productPuretitle"]
        else:
            print "没有匹配项"

if __name__ == '__main__':
    getTitle()