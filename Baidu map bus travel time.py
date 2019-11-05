#!/usr/bin/python 
# -*- coding: utf-8 -*-
# 服务文档http://lbsyun.baidu.com/index.php?title=webapi/direction-api-v2
import requests
import pandas as pd
import time

HQ = '35.79834,112.935106'
baidu = 'http://api.map.baidu.com/direction/v2/transit?output=json'
ak = 'bGmjUSC1fTrWum4GVO101GjTmq0PKjn6'

def get_routes(o):
    f1 = open(r'D:\红旗生活广场公交出行时耗.txt', 'a')
    f2 = open(r'D:\红旗生活广场公交错误.txt', 'a')
    url = baidu + '&origin=' + o + '&destination=' + HQ + '&ak=' + ak
    try:
        response = requests.get(url).json()
        result = response['result']
        o_lng = result['origin']['location']['lng']
        o_lat = result['origin']['location']['lat']
        total = result['total']
        for r in result['routes']:
            price = r['price']
            time = r['duration']
            all_info = str(o_lat) + ',' + str(o_lng) + ';' + str(total) + ';' + str(time)
            print(all_info)
            f1.write(all_info + '\n')
    except:
        f2.write(o + '\n')

xy = pd.read_excel('D:\***.xlsx',index_col=0) #存放起点坐标的文件

start = time.time()
for i in range(1,len(xy)+1):
    o = xy.get_value(i, 'xy')
    get_routes(o)
    time.sleep(2)

end = time.time()
lasttime = int((end-start))
print('耗时'+str(lasttime)+'s')
