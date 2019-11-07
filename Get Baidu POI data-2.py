#!/usr/bin/python 
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import time

f = open(r'***.txt') #格网属性表
next(f)
bounds = []
for line in f:
    line2 = line.split(',')
    latl = line2[6] #latl
    lngl = line2[7] #lngl
    latr = line2[8] #latr
    lngr = line2[9] #lngr
    bounds.append(latl + ',' + lngl + ',' + latr + ',' + lngr)

baidu = 'http://api.map.baidu.com/place/v2/search'
ak = '***' #百度地图API密钥
q = '超市'
names = []
lats = []
lngs = []
#lines = []

def bound_search(b):
    for pages in range(0,20):
        time.sleep(2)  #解决一分钟并发量限制
        poi = {'q':q, 'coord_type':'1', 'bounds':b,'output':'json', 'ak': ak, 'page_size':'20', 'page_num':pages}
        response = requests.get(baidu, params=poi).json()
        total = response['total']
        if total < 400:
            RJ = response['results']
            if RJ != None:
                for i in RJ:
                    name = i['name']
                    lat = i['location']['lat']
                    lng = i['location']['lng']
                    print(name, lat, lng)
                    #line = i['address']
                    names.append(name)
                    lats.append(lat)
                    lngs.append(lng)
                    #lines.append(line)
        else:
            print(poi['bounds'])

for r in bounds:
    bound_search(r)

#保存结果
all = {'名称':names, '纬度':lats, '经度':lngs}
stop = pd.DataFrame(all)
stop.to_excel('***.xls', sheet_name='Sheet1')
