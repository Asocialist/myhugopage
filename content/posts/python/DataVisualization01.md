---
title: 'Data Visualization 01'
date: 2025-08-15T13:53:32+09:00
# weight: 1
# aliases: ["/first"]
tags: []
author: "liuruzhi"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: true
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

## 学习numpy

- 用numpy建立数组
- 理解numpy ndarray对象的性质
- 操作numpy

-----------

1. Ndarray对象

    - 一系列同类型数据集合以0下标开始对元素索引
    - 存放同类型多维数组在内存中占有相同大小区域
    - 由一个指向数据的指针 dtype 表示形状的shape元组 跨度元组stride组成(跨度可以为负向后移动)
    `numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)`

1. dtype数据类型

     - 类似C语言数据类型
     - numpy.dtype用于描述与数组对应的内存区域是如何使用的
     - 字节顺序  是通过对数据类型预先设定 `<` 或 `>` 来决定的。 `<` 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。`>` 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。
  
    `numpy.dtype(object, align, copy)`

     - object - 要转换为的数据类型对象 align - 如果为 true，填充字段使其类似 C 的结构体。 copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用

    ```python
    import numpy as np
    student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
    a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
    print(a)
    ```

1. 数组属性

| 属性          |                   说明                   |
|:--------------|:----------------------------------------:|
| `np.size`     |        总元素数 各轴上的大小乘积         |
| `np.shape`    | dimension 数组维度  表示在各个轴上的大小 |
| `np.itemsize` |         每个元素大小以字节为单位         |
| `np.ndim`     |            数组维度的数量rank            |
| `np.flags`    |             包含内存布局信息             |
| `np.real`     |                元素的实部                |
| `np.imag`     |                   虚部                   |
| `data`        |           元素缓冲区一般不使用           |

1. 建立数组

    - `numpy.empty(shape, dtype = float, order = 'C')` numpy.empty方法建立制定形状和数据类型的数组(order为C是行优先储存F为列优先储存)

```python
# 生成随机数组
import numpy as np 
x = np.empty([3,2], dtype = int) 
print (x)
```

- `numpy.zeros(shape,dtype = float, order = 'C')`以0填充

```python
import numpy as np
 
# 默认为浮点数
x = np.zeros(5) 
print(x)
 
# 设置类型为整数
y = np.zeros((5,), dtype = int) 
print(y)
 
# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')]) 
print(z) 
```

- `numpy.ones(shape,dtype=float,order='C')` 创建指定形状的数组，数组元素以 1 来填充。

```python
import numpy as np
 
# 默认为浮点数
x = np.ones(5) 
print(x)
 
# 自定义类型
x = np.ones([2,2], dtype = int)
print(x)
```

- `numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)`numpy.zeros_like用于创建一个指定形状的数组，其中所有元素都是 0 创建与指定数组相同形状的数组

```python
import numpy as np
 
# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print(zeros_arr)
```

- `numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)`numpy.ones 和 numpy.ones_like 都是用于创建一个指定形状的数组，其中所有元素都是 1.它们之间的区别在于：numpy.ones 可以直接指定要创建的数组的形状，而 numpy.ones_like 则是创建一个与给定数组具有相同形状的数组。

```python
import numpy as np
 
# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 1 的数组
ones_arr = np.ones_like(arr)
print(ones_arr)
```
