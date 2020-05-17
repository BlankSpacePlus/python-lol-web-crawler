# coding:utf-8
import os
import requests
import random
import re
import time

# url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
# herolist = requests.get(url)  # 获取英雄列表json文件
# herolist_json = herolist.json()  # 转化为json格式
# print(herolist_json)
# heros = herolist_json['hero']
# print(heros)
# hero_name = list(map(lambda x: x['title'], heros))  # 提取英雄的名字
# print(hero_name)
# hero_number = list(map(lambda x: x['heroId'], heros))  # 提取英雄的编号
# print(hero_number)

payload = ""
# 请求头 (我在提交的时候把Cookie删了，自己可以加上.)
headers = {
    "Accept": "text/css,*/*;q=0.1",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
}

hero_id_list = [0, 1, 22, 12, 4, 15, 17, 10, 9, 20, 16, 13, 11, 19, 18, 14, 24, 25, 27, 26, 23, 28, 29, 30, 31, 32, 33,
                34, 45, 38, 44, 41, 53, 40, 54, 36, 42, 55, 75, 35, 74, 77, 76, 78, 80, 79, 82, 81, 98, 85, 86, 84,
                90, 2, 96, 5, 8, 3, 6, 21, 37, 50, 99, 7, 39, 48, 69, 51, 58, 43, 57, 59, 56, 64, 63, 68, 67, 61, 83,
                89, 62, 72, 91, 92, 101, 104, 102, 105, 106, 103, 112, 113, 115, 111, 114, 117, 120, 110, 122, 119,
                126, 143, 131, 107, 134, 121, 60, 238, 267, 254, 412, 133, 154, 127, 266, 236, 222, 157, 161, 201, 150,
                268, 429, 421, 432, 245, 223, 203, 420, 202, 136, 163, 240, 427, 164, 497, 498, 141, 516, 142, 145,
                555, 518, 517, 350, 246, 235, 523, 875]

hero_list = [0, 13, 12, 14, 12, 12, 11, 10, 10, 9, 12, 13, 11, 12, 12, 7, 12, 11, 10, 7, 11, 9, 11, 7, 8, 11, 10, 9, 12,
             7, 6, 11, 12, 11, 12, 11, 10, 13, 9, 9, 7, 6, 11, 10, 10, 11, 7, 14, 9, 8, 13, 13, 9, 9, 11, 9, 10, 8, 6,
             15, 9, 6, 14, 9, 10, 7, 6, 12, 12, 10, 9, 10, 8, 13, 8, 5, 12, 9, 5, 10, 7, 5, 8, 12, 6, 11, 7, 10, 6, 12,
             5, 10, 9, 6, 10, 9, 9, 9, 9, 9, 6, 7, 7, 7, 7, 6, 6, 7, 8, 8, 10, 5, 4, 5, 7, 9, 9, 8, 4, 7, 7, 5, 4, 4,
             4, 8, 4, 3, 3, 6, 3, 3, 3, 3, 4, 6, 5, 3, 2, 4, 6, 4, 4, 3, 3, 4, 3, 2, 2]

for i in range(111, 149):
    num = hero_list[i]
    path = "D:/skins/hero" + str(i)
    # 进入创建好的文件夹
    os.chdir(path)
    for j in range(num):
        # 拼接url
        temp_num = str(j) if j >= 10 else '0'+str(j)
        hero_link = 'https://game.gtimg.cn/images/lol/act/img/skin/' + 'big' + str(hero_id_list[i]) + '0' + temp_num + '.jpg'
        print(hero_link)
        # 请求url
        im = requests.request("GET", hero_link, data=payload, headers=headers)
        # im = requests.get(hero_link)
        if im.status_code == 200:
            # 写入文件
            open(str(j+1) + '.jpg', 'wb').write(im.content)
            # time.sleep(random.randint(10, 15))
    time.sleep(random.randint(20, 25))
