#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:32:55 2021

@author: muzian
"""

import requests
import pandas as pd

stock = "sz000009"
r = requests.get("http://hq.sinajs.cn/list="+stock)

if r.status_code == 200:
    print(r.text)
    
    stock_list = []
    split_lines = r.text.splitlines()
    
    for line in split_lines:
        # var hq_str_s_sz000009="中国宝安,18.62,-0.38,-2.00,741728,139476";
        stock_id = line [line.find("=")-8:line.find("=")]
        right_str = line[line.find("\"")+1:line.rindex("\"")]
        
        if len(right_str)>0:
            stock_field_list = right_str.split(",")
            stock_field_list[1] = round(float(stock_field_list[1]),3)
            
            if stock_field_list[1] > 0:
                stock_field_list.insert(0,stock_id)
                stock_list.append(stock_field_list)
    print(stock_list)
    
    df = pd.DataFrame(stock_list,columns=['股票代码','股票名称','今日开盘价','昨日收盘价','当前价格',
                                          '今日最高价','今日最低价','竞买价','竞卖价','成交量','成交额','买一申请',
                                          '买一报价','买二申请','买二报价','买三申请','买三报价','买四申请','买四报价','买五申请',
                                          '买五报价','卖一申请','卖一报价','卖二申请','卖二报价','卖三申请','卖三报价','卖四申请',
                                          '卖四报价','卖五申请','卖五报价','日期','时间',"是否收盘"])
    
    df.to_csv('realtimedata.csv',index=False)
    