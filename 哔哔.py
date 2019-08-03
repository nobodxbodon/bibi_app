# -*- coding:utf8 -*-
import json
import os

当前目录内容 = os.listdir(".")
所有帖子 = []
各用户帖子 = {}

for 用户 in 当前目录内容:
    if(os.path.isdir(用户) and 用户!=".git"):
        for 帖子 in os.listdir(用户):
            if(帖子.endswith(".json")):
                with open(用户 + "/" + 帖子) as 帖子内容:
                    描述 = json.load(帖子内容)
                    描述["用户"] = 用户
                    if "帖子" in 描述["引用"]:
                        回复对象 = 描述["引用"]["用户"]
                        回复帖子 = 描述["引用"]["帖子"]
                        各用户帖子[回复对象][回复帖子 + ".json"]["回复"] = 描述
                    else:
                        所有帖子.append(描述)
                        各用户帖子[用户] = {帖子: 描述}

for 帖子 in 所有帖子:
    print(帖子["用户"] + ": " + 帖子["题目"] + " -- " + 帖子["内容"])
    if "回复" in 帖子:
        回复 = 帖子["回复"]
        print(回复["用户"] + "回复: " + 回复["题目"] + " -- " + 回复["内容"])