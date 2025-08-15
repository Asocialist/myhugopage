---
title: 'Data Visualization 00'
date: 2025-08-15T13:53:32+09:00
# weight: 1
# aliases: ["/first"]
tags: []
author: "liuruzhi"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "study python data visualization"
canonicalURL: ""
disableHLJS: false
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
cover:
    image: "" # image path/url
    alt: "" # alt text
    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
editPost:
    URL: "https://github.com/Asocialist/myhugopage/tree/main/content/"
    Text: "Suggest Changes" # edit text
    appendFilePath: true # to append file path to Edit link
---

## 学习python data visualization

- 复习python 学习 matplolib pandas seaborn 更方便的绘制研究会用到的图表
- 比较r语言 python用到的更多
- 能够独立绘制统计图表和进行数据分析为目的

### python 复习

1. 数据结构复习:
   1. list 任意对象 有序集合 `my_list = []` 注意元素可重复可以是不同类型
   2. tuple 有序 不可变 可重复 相当于一个列表但不可变 `my_tuple = ()`
   3. dictionary 储存键值对(key-value pairs) 键必须唯一且不可变 可变的是可以增删键值对 python3.7版本以后为有序  
     `mydic = {}` `another_dict = dict()`
     例子

     ``` python
        student_info = {
        "name": "Li Hua",
        "student_id": 20250815,
        "courses": ["Math", "Physics"],
        "age": 20
        }
     ```

1. 配置环境和包的安装
   1. `pip install pandas matplotlib seaborn numpy` matplotlib seaborn用于绘图和可视化  numpy he pandas 用于分析数据
   1. anaconda 管理python

1. 数据处理
   - Numpy 管理数组 `import numpy as np`

     -  
