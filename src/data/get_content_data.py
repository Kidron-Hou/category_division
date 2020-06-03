#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : get_content_data.py
# @Description: 获取去标签后的文本数据
# @Time       : 2020-5-30 上午 11:09
# @Author     : Hou

import os
import pandas as pd
import pymysql.cursors


def get_id_list():
    original_data = pd.read_excel(os.path.join(os.path.abspath('../..'), 'data', 'raw', 'filtered_data.xlsx'))
    id_series = original_data['id']
    id_list = id_series.to_numpy()
    return id_list


def get_content_data(id_list):
    """获取去标签后的文本数据"""
    connection = pymysql.connect(host='58.59.18.101',
                                 port=3306,
                                 user='data',
                                 password='data12399123',
                                 database='bidding_data',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    content_df = pd.DataFrame(columns=('bulletin_id', 'content', 'partition_key'))
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `bidding_bulletin_text` where bulletin_id= %s"
            # 获取2000条数据进行测试
            for index in range(2001):
                cursor.execute(sql, (id_list[index],))
                result = cursor.fetchone()
                # print(result)
                content_df.loc[index] = result

    finally:
        connection.close()

    return content_df


if __name__ == '__main__':
    id_list = get_id_list()
    content_df = get_content_data(id_list)
    content_df.to_excel(os.path.join(os.path.abspath('../..'), 'data', 'processed', 'content_text_data.xlsx'))


