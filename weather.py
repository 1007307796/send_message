#/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import re
import sys
import json
#reload(sys)
#sys.setdefaultencoding('utf-8')
 
def get_text():
    url = "http://www.tianqi.com/taoyuan/life.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url=url,headers=headers,verify=False)
 
    html = response.text
    html_xpath = etree.HTML(html)
 
    rain = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[1]/p/text()')[0]
    #clothes = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[6]/p/text()')[0]
    ziwaixian = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[3]/p/text()')[0]
    #travel = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[7]/p/text()')[0]
    #shaiyifu = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[8]/p/text()')[0]
 
    url2 = "http://www.tianqi.com/taoyuan/"
    response2 = requests.get(url=url2,headers=headers,verify=False)
    html2 = response2.text
    html_xpath2 = etree.HTML(html2)
    wendu = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/p/b/text()')[0]
    #shidu = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[4]/b[1]/text()')[0]
    #fengxiang = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[4]/b[2]/text()')[0]
    tianqi = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/span/b/text()')[0]
    wen = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/span/text()')[0]
    pm = html_xpath2.xpath("/html/body/div[@class='weatherbox']/div[@class='wrap1100']/div[@class='left']/dl[@class='weather_info']/dd[@class='kongqi']/h6/text()")[0]
    matchrule = re.compile(r'([0-9-]+|PA[/+]+)')
    match_out = matchrule.findall(ziwaixian)
    spf = 'SPF:' + match_out[0] + ',  ' + match_out[1]
    #情话api
    params = {'key': 'key'}
    word = requests.get('http://api.tianapi.com/txapi/saylove/index', params=params,verify=False)
    result = json.loads(word.text)
    loveword = result['newslist'][0]['content']
    text_mes = '\n' +"宝贝早安呀" + '\n'+"今日天气：" + tianqi + '，'+ pm +'\n' + '今日温度：' \
               + wen +'，' + '当前温度：' + wendu +'℃' + ',' + rain + '\n'  + spf + '\n' + loveword
    return text_mes