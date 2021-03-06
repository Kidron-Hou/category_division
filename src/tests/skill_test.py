#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : skill_test.py
# @Description:
# @Time       : 2020-6-1 上午 10:20
# @Author     : Hou

import re

pattern_after = re.compile('预中标公告 |评审公示 |需求评审 |预中标公示 |预审结果公示 |预审结果公告 |候选人公告 |候选人公示 |候选人结果公示 |候选人结果公告 |'
                 '成交公告 |成交通告 |成交公示 |合同公示 |中选公告 |中选公示 |合同公告 |信息公示表 |结果公告 |结果公示 |结果通知书 |终止公告 |'
                 '终止公示 |失败公告 |失败的公告 |作废公告 |废标公告 |流标公示 |流标公告 |流标通知|无效公告 |'
                 '中标候选人 |中标候选人：|中标候选人:|结果公示表 |中标人：|中标公示 |中标单位：|'
                 '中标单位:|中标单位 |中标人 |中 标 人 |中标人为|中标人公示 |中标候选单位：|中标供应商 |供应商：|供应商名称：|供应商名称 |中标人名称：|中标单位名称：|中标单位名称 |评标结果：|供应商信息：|'
                 '成交供应商 |成交公告：|中标金额：|中标候选人单位名称 |中标人\(乙方\)：|供应商（乙方）：|评标报告：|中选人名称：|'
                 '成交人：|中标通知书 |成交单位：|中标内容：|中标企业|中标项目名称：'
                 '预审公告 |邀请招标 |谈判公告 |竞争性谈价 |竞争性谈判 |询价公告 |来源公告 |单一来源采购 |采购公告 |'
                 '磋商公告 |竞争性磋商 |竞价公告 |遴选公告 |议价公告 |议价信息 |网络竞价 |出让公告 |土地出让 |挂牌出让 |拍卖公告 |公开招标 |'
                 '招标公告 |项目公告 |采购公示 |采购计划 |采购预告 |采购需求 |采购申前公示 |采购前公示 |需求公告 |招标预告 |征求意见 |预公告 |'
                 '需求信息 |需求计划 |选择计划 |预公示 |启动公示 |招标公示 |标前公示 |需求公示 |销售预告 |项目申前公示 |变更公告 |更正公告 |'
                 '变更说明 |推迟 |暂停公告 |变更计划 |变更文件 |调整通知 |变更公示 |更改为|更正为|延期 |变更通知 |补充说明 |补充通知 |补充文件 |补充招标公告 |'
                 '招标控制价 |补充公告 |项目答疑 |变更答疑 |补疑 |答疑明细 |补遗 |澄清 |答疑澄更 |评标 |流标 |废标 |资格要求 |资格要求：|资格条件：|采购通知 |供应商基本条件：|竞价须知 |'
                 '投标人资格 |投标人资格条件 |询价通知书 |采购说明：|报价须知：|报名公告 |招标文件 |货物采购 |服务采购 |工程分包 |错字更正 |'
                 '关于暂停|更改通知|澄清公告|抽签公告|更正公示 |资格审核 |答疑变更|项目要求：|单轮竞价 |抽签时间及地点 ')

key_words = ['预中标公告 ','评审公示 ','需求评审 ','预中标公示 ','预审结果公示 ','预审结果公告 ','候选人公告 ','候选人公示 ','候选人结果公示 ','候选人结果公告 ','成交公告 ','成交通告 ','成交公示 ','合同公示 ','中选公告 ','中选公示 ','合同公告 ','信息公示表 ','结果公告 ','结果公示 ','结果通知书 ','终止公告 ','终止公示 ','失败公告 ','失败的公告 ','作废公告 ','废标公告 ','流标公示 ','流标公告 ','流标通知','无效公告 ','中标候选人 ','中标候选人：','结果公示表 ','中标人：','中标公示 ','中标单位：','中标单位:','中标单位 ','中标人 ','中 标 人 ','中标人为','中标人公示 ','中标候选单位：','中标供应商 ','供应商：','供应商名称：','供应商名称 ','中标人名称：','中标单位名称：','中标单位名称 ','评标结果：','供应商信息：','成交供应商 ','成交公告：','中标金额：','中标候选人单位名称 ','中标人\(乙方\)：','供应商（乙方）：','评标报告：','中选人名称：','成交人：','中标通知书 ','成交单位：','中标内容：','中标企业','中标项目名称：预审公告 ','邀请招标 ','谈判公告 ','竞争性谈价 ','竞争性谈判 ','询价公告 ','来源公告 ','单一来源采购 ','采购公告 ','磋商公告 ','竞争性磋商 ','竞价公告 ','遴选公告 ','议价公告 ','议价信息 ','网络竞价 ','出让公告 ','土地出让 ','挂牌出让 ','拍卖公告 ','公开招标 ','招标公告 ','项目公告 ','采购公示 ','采购计划 ','采购预告 ','采购需求 ','采购申前公示 ','采购前公示 ','需求公告 ','招标预告 ','征求意见 ','预公告 ','需求信息 ','需求计划 ','选择计划 ','预公示 ','启动公示 ','招标公示 ','标前公示 ','需求公示 ','销售预告 ','项目申前公示 ','变更公告 ','更正公告 ','变更说明 ','推迟 ','暂停公告 ','变更计划 ','变更文件 ','调整通知 ','变更公示 ','更改为','更正为','延期 ','变更通知 ','补充说明 ','补充通知 ','补充文件 ','补充招标公告 ','招标控制价 ','补充公告 ','项目答疑 ','变更答疑 ','补疑 ','答疑明细 ','补遗 ','澄清 ','答疑澄更 ','评标 ','流标 ','废标 ','资格要求 ','资格要求：','资格条件：','采购通知 ','供应商基本条件：','竞价须知 ','投标人资格 ','投标人资格条件 ','询价通知书 ','采购说明：','报价须知：','报名公告 ','招标文件 ','货物采购 ','服务采购 ','工程分包 ','错字更正 ','关于暂停','更改通知','澄清公告','抽签公告','更正公示 ','资格审核 ','答疑变更','项目要求：','单轮竞价 ','抽签时间及地点 ']
str_content = """
"contentText": " 酒泉元隆工程咨询有限公司受瓜州县县乡道路管理站的委托，对G312线七瓜公路项目电力线路迁改工程(施工一标段）进行招标， 并于2020-05-08 09:00:00开标、评标，开评标会结束后根据有关法律、法规要求，现对中标候选人进行公示。 特此公示 标段(包)编号：gzjt20200416000200101 标段(包)名称：G312线七瓜公路项目电力线路迁改工程(施工一标段） 招标代理机构：酒泉元隆工程咨询有限公司 招标人：瓜州县县乡道路管理站 经评标委员会评审，确定中标候选人为: 第一中标候选人:酒泉市兴达建筑安装工程有限责任公司 第二中标候选人:甘肃宝光电力安装工程有限公司 第三中标候选人:广东联网电力有限公司",
"""

print(pattern_after.findall(str_content))