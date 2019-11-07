#!/usr/bin/python 
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import time

baidu = 'http://api.map.baidu.com/geoconv/v1/'
ak = 'nmMNc8yKPk9j5P9Q7pTrRGxjwGShT1S7'

corf = 5
# 1：GPS设备获取的角度坐标，WGS84坐标
# 2：GPS获取的米制坐标、sogou地图所用坐标
# 3：google地图、soso地图、aliyun地图、mapabc地图和amap地图所用坐标，国测局（GCJ02）坐标
# 4：3中列表地图坐标对应的米制坐标
# 5：百度地图采用的经纬度坐标
# 6：百度地图采用的米制坐标
# 7：mapbar地图坐标
# 8：51地图坐标

cort = 6
# 5：bd09ll(百度经纬度坐标);
# 6：bd09mc(百度米制经纬度坐标)


def trans_cor(cor):
    c = {'coords':cor,'from':corf,'to':cort, 'ak': ak}
    response = requests.get(baidu, params = c).json()
    result = response['result']
    for i in result:
        lat = i['y']
        lng = i['x']
        print(lat,lng)

xy = ['128.543,37.065']
trans_cor(xy)
