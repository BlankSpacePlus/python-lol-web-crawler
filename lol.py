# coding:utf-8
import os
import random
import time

import requests

url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
print(herolist_json)
heros = herolist_json['hero']
print(heros)
hero_name = list(map(lambda x: x['title'], heros))  # 提取英雄的名字
print(hero_name)
hero_number = list(map(lambda x: x['heroId'], heros))  # 提取英雄的编号
print(hero_number)


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        print("开始下载(%s)的图片" % (hero_name[i]))
        # 创建文件夹
        os.mkdir("D:/LOL/LOL" + hero_name[i])
        # 进入创建好的文件夹
        os.chdir("D:/LOL/LOL" + hero_name[i])
        i += 1
        for k in range(15):
            # 拼接url
            onehero_link = 'https://game.gtimg.cn/images/lol/act/img/skin/' + 'big' + j + '00' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


downloadPic()
