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
    latl = line2[-4] #latl左下角经度
    lngl = line2[-3] #lngl左下角纬度
    latr = line2[-2] #latr右上角经度
    lngr = line2[-1] #lngr右上角纬度
    bounds.append(latl + ',' + lngl + ',' + latr + ',' + lngr)

baidu = 'http://api.map.baidu.com/place/v2/search'
ak = '***' #百度地图API密钥
q = '超市'
names = []
lats = []
lngs = []

def bound_search(b):
    for pages in range(0,20):
        poi = {'q':q,'bounds':b,'output':'json', 'ak': ak, 'page_size':'20', 'page_num':pages}
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
                    names.append(name)
                    lats.append(lat)
                    lngs.append(lng)
        else:
            print(poi['bounds'])

for r in bounds:
    time.sleep(1)  #解决一分钟并发量限制
    bound_search(r)

#保存结果
all = {'名称':names, '纬度':lats, '经度':lngs}
stop = pd.DataFrame(all)
stop.to_excel('***.xls', sheet_name='Sheet1')
