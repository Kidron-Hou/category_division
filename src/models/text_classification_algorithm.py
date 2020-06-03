#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : text_classification_algorithm.py
# @Description: 研究文本分类算法
# @Time       : 2020-6-3 下午 2:19
# @Author     : Hou

import pandas as pd
import os

raw_data = pd.read_excel(os.path.join(os.path.abspath('../..'), 'data','external','复旦大学中文文本分类语料.xlsx'), 'sheet1')

print(raw_data.info())