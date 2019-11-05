import requests
import pandas as pd

#D = '32.093502,118.803714' #终点坐标

baidu = 'http://api.map.baidu.com/direction/v2/transit?output=json&tactics_incity=4'

ak = 'nmMNc8yKPk9j5P9Q7pTrRGxjwGShT1S7' #申请的密钥 http://lbsyun.baidu.com/apiconsole/key?application=key

def get_routes(o, d): #设置请求参数
    url = baidu + '&origin=' + o + '&destination=' + d + '&ak=' + ak
    try:
        response = requests.get(url).json()
        result = response['result']
        o_name = result['origin']['city_name']
        total = result['total']
        r = result['routes'][0]
        time = r['duration']
        price = 0
        for p in r['price_detail']:
            price += p['ticket_price']
        t = 0
        for s in r['steps']:
            type = s[0]['vehicle_info']['type']
            if type == 3:
                t = t + 1
        all_info = o_name + ';' + str(total) + ';' + str(time) + ';' + str(price) + ';' + str(t - 1) #可返回O点ID、OD间公交出行方案数量、OD间公交出行时间、OD间公交出行费用、OD间公交出行换乘次数
        return all_info
    except:
        all_info = '无数据'+ ';' + 'null'+ ';' + 'null'+ ';' + 'null'+ ';' + 'null'#可能会因OD间无公交出行方案，返回null值
        return all_info

xy = pd.read_excel('H:/NJ/inhi/街道坐标.xlsx',index_col=0) #批量读取O点坐标，与PY文件在一个文件夹中

f = open(r'H:/NJ/inhi/街道出行时间.txt', 'a') #保存返回参数文件，与PY文件在一个文件夹中
for i in range(0,86):
    o = xy.get_value(i, 'xy')
    o_name = xy.get_value (i, '名称')
    for j in range (0,86):
        d_name = xy.get_value (j, '名称')
        d = xy.get_value(j, 'xy')
        print(str(i) + ';' + o_name + ';'+ d_name + ';' + get_routes(o, d))
        f.write(str(i) + ';' + o_name + ';'+ d_name + ';' + get_routes(o, d) + '\n')