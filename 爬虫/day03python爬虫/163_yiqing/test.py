# =============================================
# --*-- coding: utf-8 --*--
# @Time    : 2020-03-27
# @Author  : 不温卜火
# @CSDN    : https://blog.csdn.net/qq_16146103
# @FileName: Real-time epidemic.py
# @Software: PyCharm
# =============================================
import requests
import pandas as pd
import json
import time

pd.set_option('max_rows', 500)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}

url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'  # 定义要访问的地址
r = requests.get(url, headers=headers)  # 使用requests发起请求

print(r.text)

data_json = json.loads(r.text)
data = data_json['data']
data_province = data['areaTree'][2]['children']
areaTree = data['areaTree']


class spider_yiqing(object):

    # 将提取数据的方法封装成函数
    def get_data(data, info_list):
        info = pd.DataFrame(data)[info_list]  # 主要信息

        today_data = pd.DataFrame([i['today'] for i in data])  # 提取today的数据
        today_data.columns = ['today_' + i for i in today_data.columns]

        total_data = pd.DataFrame([i['total'] for i in data])
        total_data.columns = ['total_' + i for i in total_data.columns]

        return pd.concat([info, total_data, today_data], axis=1)

    def save_data(data, name):
        file_name = name + '_' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + '.csv'
        data.to_csv(file_name, index=None, encoding='utf_8_sig')
        print(file_name + '保存成功！')

    if __name__ == '__main__':
        today_province = get_data(data_province, ['id', 'lastUpdateTime', 'name'])
        # today_world = get_data(areaTree, ['id', 'lastUpdateTime', 'name'])
        # save_data(today_province, 'today_province')
        # save_data(today_world, 'today_world')
