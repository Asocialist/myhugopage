---
title: 'DataVisual02'
date: 2025-08-18T16:15:48+09:00
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
---

## 学习pandas处理表格

- 用pandas建立表格
- 学习Series(一维) DataFrame(二维) 和 Categorical(三维或可变维)数据结构
- 处理表格导入数据

------

### Series 数据结构

1. 一个含有索引的一维数组 左侧的索引(index)可以自动生成从0开始或指定 右侧的值(value)
1. Series可以容纳不同数据类型的元素 int float string 和python对象
1. 大小在创建后不变 可以通过 append 和delete 改变
1. 可以自动对齐和添加名称

- 创建 Series `pd.Series(data = none, index = none, name = none,dtype = none, copy = False, fastpath = False)`
  - data : 数据 可以为列表 数组 字典 标量 空时则建立一个空的series
  - index : 索引
  - name : 名称
  - dtype : 数据类型
  - copy : 是否复制数据
  - fastpath : 快速路径启用 提升性能

```python
import pandas as pd

# 创建一个Series
s = pd.Series([1, 2, 3, 4, 5], name ='MySeries')
print(s)

custom_index = ['a', 'b', 'c', 'd', 'e']
s_with_index = pd.Series([1, 2, 3, 4, 5], index=custom_index, name='MySeriesWithIndex')
print(s_with_index)

```

```python
import pandas as pd
#自己设置索引并访问
a = [ "wikipedia", "google", "facebook", "twitter" ]
myvar = pd.Series(a, index = ["a", "b", "c", "d"])
print(myvar["c"])
```

```python
import pandas as pd

# 创建 Series
data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)

# 查看基本信息
print("索引：", s.index)
print("数据：", s.values)
print("数据类型：", s.dtype)
print("前两行数据：", s.head(2))

# 使用 map 函数将每个元素加倍
s_doubled = s.map(lambda x: x * 2) #lamda 匿名函数 参数 : 表达式 表达式的结果就是返回值
print("元素加倍后：", s_doubled)

# 计算累计和
cumsum_s = s.cumsum()
print("累计求和：", cumsum_s)

# 查找缺失值（这里没有缺失值，所以返回的全是 False）
print("缺失值判断：", s.isnull())

# 排序
sorted_s = s.sort_values()
print("排序后的 Series：", sorted_s)
```

### DataFrame

1. 二维结构 可以看作多个series对象组成的节点
1. 不同的列可以包含不同的数据类型
1. 索引有行索引和列索引 类似excel中的行号和列标
1. 大小可变 可自动对齐 可以包含缺失数据 有时间序列支持
1. 可以读取和写入数据 支持切片 索引 子集等分割操作

- `pd.DataFrame(data=None,index=None,columns=None,dtype=None,copy=False)`
  - data : 数据 字典 二维数组 等 (字典建立 key就是列名)
  - index : 行索引
  - columns : 列索引
  - dtype : 数据类型
  - copy : 是否复制数据

```python
import pandas as pd

# 创建 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# 查看前两行数据
print(df.head(2))

# 查看 DataFrame 的基本信息
print(df.info())

# 获取描述统计信息
print(df.describe())

# 按年龄排序
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)

# 选择指定列
print(df[['Name', 'Age']])

# 按索引选择行
print(df.iloc[1:3])  # 选择第二到第三行（按位置）

# 按标签选择行
print(df.loc[1:2])  # 选择第二到第三行（按标签）

# 计算分组统计（按城市分组，计算平均年龄）
print(df.groupby('City')['Age'].mean())

# 处理缺失值（填充缺失值）
df['Age'] = df['Age'].fillna(30)

# 导出为 CSV 文件
df.to_csv('output.csv', index=False)
```

```python
#使用字典创建

import pandas as pd

data ={'Site': ['wikipedia', 'google', 'facebook', 'twitter'],
        'Age': [20, 22, 25, 18],
        'Likes': [1000, 2000, 1500, 800]}

df = pd.DataFrame(data)
print(df)
```

```python
#使用nadarrays创建 

import numpy as np
import pandas as pd

ndarrays = np.array([['google',20],['weki',10],['facebook',30],['twitter',40]])
df = pd.DataFrame(ndarrays, columns=['Site', 'Age']) # 添加列名
print(df)
print(df.dtypes)
```

- 通过nadarrays创建时注意ndarrays的长度必须相同,如果传递了index则索引的长度应该等于数组的长度 如果没有传递索引在默认为range(n)n为数组长度

- 索引补充:
  - 获取列名和行名: `df.columns` `df.index`
  - `df.['column']` `df.loc[:,['column']]` `df.iloc[:,[columnNum']]`获取列 获取行 `df.iloc[index,:]` `df.loc[index,:]`
  - 选取具体元素 `df.iloc[index,columnNum]` `df.loc[[index],['column']]`
  - 多重索引: 使用loc方法选择数据
    - 比如:两层索引 df.index(['X','year'])   0级索引为"X" 1级索引为"year"则`df.loc[('X',slice(None),'Value')]`来选择因为可能行名有重复这里不能用`:`来代替slice

```python
# import pandas as pd

df = pd.DataFrame(dict(X= ['A', 'B', 'C','A','B','C'],year=[2010,2011,2012,2013,2014,2015],Value=[1,2,3,4,5,6]))
df = df.set_index(['X', 'year'])
print(df)
print(df.index)
print(df.loc[('A', 2010), 'Value']) # 选择 X 为 'A' 且 year 为 2010 的 Value 列
print(df.loc[('A', slice(None)), 'Value'])  # 示例：选择 X 为 'A' 的所有行的 Value 列
```

- 建立新的空数据框 `df_empty=pd.DataFrame(columns=['X','Y','Z'])`
- 网络型分布数据创建 `np.meshgrid()`在两个坐标轴上的电在平面上画网格 三维差值重要

```python
import pandas as pd

# 1. 创建带列名的空 DataFrame
df_empty = pd.DataFrame(columns=['X', 'Y', 'Z'])

# 准备一个列表来收集新行
rows_to_add = []

# 2. 假设我们在一个循环中生成数据
for i in range(5):
    # 将新行创建为一个只有一行的小 DataFrame
    new_row = pd.DataFrame([{'X': f'A{i}', 'Y': i * 10, 'Z': True}])
    rows_to_add.append(new_row)

# 3. 循环结束后，一次性合并所有新行
if rows_to_add: # 确保列表不为空
    df_final = pd.concat([df_empty] + rows_to_add, ignore_index=True)
else:
    df_final = df_empty

print(df_final)
```

```python
import numpy as np

# 1. 定义 X 轴和 Y 轴上你关心的点
x = np.array([-1, 0, 1])
y = np.array([-2, 0, 2])

# 2. 创建坐标矩阵
XX, YY = np.meshgrid(x, y)
print(XX)
print(YY)

Z = XX**2 + YY**2
print(Z)
```

### Categorical 分类

1. 用于承载基于证书的类别展示或编码的数据.可以看作包含了额外信息的列表,额外的信息指的就是不同的类别决定了数据的分析方式
1. `pd.Categorical(values, categories=None, ordered=False)`一个分类数据不仅包含分类变量本身还可能好饱变量的不同类别 可以在创建时设定好类别
   - categories: 指定类别（默认是 values 里去重后的唯一值，按出现顺序）。
   - values: 要转换的数据（list / ndarray / Series）。
   - ordered: 是否是有序类别（默认 False，表示无序）
1. 已经创建的分类数据或数据框 可硬使用 `*.astype(dtype)`来制定类别覆盖默认排序
   - dtype: 可以是 "category"，CategoricalDtype，int，float 等等。
   - 如果写 .astype("category")，只是把数据转成 分类数据类型，但不会自动改变类别顺序。
   - 只对Series和DataFrame有用返回的是新的Series

```python
import pandas as pd

Cut =["Fair", "Good", "Very Good", "Excellent"]
Cut_Factor = pd.Categorical(Cut)
print(Cut_Factor)
Cut_Factor = pd.Categorical(Cut, categories=["Fair", "Good", "Very Good", "Excellent"], ordered=True)
print(Cut_Factor)
new_order = ["Good", "Fair", "Very Good", "Excellent"]

Cut_Factor2 = pd.Categorical(Cut, categories=new_order, ordered=True)
print(Cut_Factor2)
```

### 表格操作

1. 表格变换

   - 绘图时如果导入的数据是二维数据列表,需要使用pd.melt()函数将二维数据列表的数据框转换成一位数据列表
   - `pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name="value", col_level=None, ignore_index=True)`
     - frame 是传入的数据
     - id_vars是保存的列 value_vars需要熔化的列 var_name是熔化之后列名那一列的名字  value_name是熔化之后数值那一列的名字
     - ignore_index 是重新编码
   - `DataFrame.pivot_table(data=None,values=None,index=None,columns=None,aggfunc='mean',fill_value=None,margins=False,margins_name='All',dropna=True,observed=False,)` 将行列重新排列 进行分组统计类似excel的透明表
     - aggfunc: 聚合函数，默认 mean，可以是 "sum", "count", "max", "min", np.median 等
     - fill_value: 缺失值填充值。
     - margins: 是否加上行/列合计（类似 Excel 的 “总计”）。

```python
#二维数据列表转换为一维数据列表
import pandas as pd

# 创建一个 二维数据列表

df = pd.DataFrame({'X' : ['A', 'B', 'C'],
                     '2010' : [1, 2, 3],
                        '2011' : [4, 5, 6]
                        })
# 打印原始数据框
print(df)
# 使用 pd.melt() 将二维数据列表转换为一维数据列表
# 将宽数据转换为长数据将多行聚集成列,
df_melt  = pd.melt(df,id_vars='X', var_name='Year', value_name='Value')
print(df_melt)

df_pivot = df_melt.pivot(index='X', columns='Year', values='Value')
df_pivot = df_pivot.reset_index()
print(df_pivot)
```

1. 变量变换

    - 对某一列的变量进行排序处理. 产生新的列
    - 基础运算 `df["Ratio"] = df["B"] / df ["A"]`
    - 函数运算 `df.map()`针对series逐个元素映射 `.apply()`针对series和dataframe 逐个元素/列/行操作 `.applymap()`专门针对dataframe
    - 缺失值变换 `df.fillna()`

```python
# map: Series
df["A_squared"] = df["A"].map(lambda x: x**2)

# apply: Series
df["B_sqrt"] = df["B"].apply(np.sqrt)

# apply: DataFrame
df_sum = df.apply(sum, axis=0)  # 每列求和
df_row_sum = df.apply(sum, axis=1)  # 每行求和
```

```python
#归一化
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5]})

# 归一化到 [0,1]
df["A_minmax"] = (df["A"] - df["A"].min()) / (df["A"].max() - df["A"].min())

# 标准化 (均值0, 方差1)
df["A_zscore"] = (df["A"] - df["A"].mean()) / df["A"].std()

print(df)

```

1. 表格排序和拼接
   1. 排序
      - `.sort_values(by="")`按值排序  
      - `.sort_index()`按索引排序

   1. 拼接
      - 在已有的数据框的基础上添加新的行/列或者在纵/横向添加另外一个表格
      - `pd.concat([df1,df2],axis)` 沿轴拼接 axis=0为行(纵向) axis=1为列(横向)
      - `df_new=df.append(df_add)`也是添加行
      - `pd.merge()`类似SQL的join
      - `*.drop(labels="",axis=Num,inplace=True)`删除行列 labels是要删除行列的名字 axis默认为0删除行 inplace=False默认删除操作不改变原数据而是返回一个删除操作后的新的DataFrame若为true则会在原数据上改变且无法返回 删行可以按index来

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Cathy", "David"],
    "Age": [25, 30, 22, 35],
    "Score": [88, 92, 95, 70]
})

# 按 Age 升序
print(df.sort_values(by="Age"))

# 按 Score 降序
print(df.sort_values(by="Score", ascending=False))

# 多列排序（先 Age 升序，再 Score 降序）
print(df.sort_values(by=["Age", "Score"], ascending=[True, False]))

df2 = df.set_index("Name")

# 按索引升序
print(df2.sort_index())

# 按索引降序
print(df2.sort_index(ascending=False))
```

```python
df1 = pd.DataFrame({"ID": [1, 2], "Score": [90, 95]})
df2 = pd.DataFrame({"ID": [3, 4], "Score": [88, 92]})

# 行拼接（纵向，像数据库的 UNION ALL）
print(pd.concat([df1, df2]))

# 列拼接（横向）
df3 = pd.DataFrame({"Name": ["Alice", "Bob"]})
print(pd.concat([df1, df3], axis=1))
```

```python
import pandas as pd
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Cathy"]
})

scores = pd.DataFrame({
    "ID": [1, 2, 4],
    "Score": [88, 92, 95]
})

# 内连接（只保留匹配 ID）on是保留的 how参数指定连接方式
print(pd.merge(students, scores, on="ID", how="inner")) 

# 左连接（保留左表全部）
print(pd.merge(students, scores, on="ID", how="left"))

# 右连接（保留右表全部）
print(pd.merge(students, scores, on="ID", how="right"))

# 外连接（保留所有 ID）
print(pd.merge(students, scores, on="ID", how="outer"))

print(students.drop(labels=['Name'], axis=1, inplace=False))  
import pandas as pd

df = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
})

# 删除行（按索引）
df1 = df.drop(1)   # 删除索引=1 的那一行
print(df1)

# 删除列（按列名）
df2 = df.drop('B', axis=1)   # 删除列 'B'
print(df2)

```

1. 表格分组

- `df.groupby()`按数据类别进行分类操作 `df.groupby('列名')` `df.groupby(['列名1', '列名2'])`
- 先按照某个键分组 再对每个组进行计算 最后将结果拼回来
- 分组之后可以用.apply()来进行自定义操作 通过lamda函数来执行复杂操作通过[]来选取想要操作的列
- `df.aggregate()`分组聚合 .agg()多个自定义函数
- `df.transform()`分组运算 实现SQL中分组运算的操作
- `df.filter()` 分组筛选
- 总结: 先分组再选择列之后进行相应操作 `df.goupby('column')['value'].transform(lambda x: x/ s.sum())`

```python
import pandas as pd

df = pd.DataFrame({
    '班级': ['一班', '一班', '二班', '二班', '三班'],
    '姓名': ['小明', '小红', '小刚', '小丽', '小华'],
    '成绩': [85, 90, 78, 88, 92],
    '年龄': [15, 14, 16, 15, 14]
})
print(df)

# 按班级分组，计算每个班级的平均成绩
print(df.groupby('班级')['成绩'].mean()) #通过[]选取列

# 按班级和年龄分组，计算每个组合的平均成绩
print(df.groupby(['班级','年龄'])['成绩'].mean())

#分组后统计多个指标
print(df.groupby('班级').agg({
    '成绩': ['mean', 'max', 'min'],  # 平均值、最大值、最小值
    '年龄': 'mean'
}))
```

### 数据导入导出

1. CSV
   - `pd.read_csv('path/Data.csv',sep=",",header=0,names=None,index_col=None,encoding="utf-8")`
      - sep指定分隔符
      - header指定行号为列标题默认为0可以设置为None
      - names自定义列名
      - index_col 用作索引的列号或名
      - dtype 强制转换格式
      - skiprows逃过开头指定行数 或传入一个行号的列表
      - na_values 指定哪些值为缺失值
      - skipfooter跳过文件结尾的指定行数
      - nrows 读取前n行
   - `df.toces('path/output.csv',sep=",",index=False,header=True,cloumns=['A','B'])`
      - sep 分隔符
      - index 是否写入行索引
      - columns 写入指定的列
      - header 是否写入列名
      - mode 写入文件的格式
      - encodeing
      - line_terminator 定义行结束符默认\n
      - quotechar 设置用于引用的字符默认"
      - date_format自定义日期格式
      - doublequote 若为true则将包含引号的文本用双引号括起来

1. txt
   - `np.loadtxt()`注意txt文件中必须要含有相同数量的数据 会读取并储存为ndarray数组在使用pd.DataFrame函数转换为DataFrame格式
   - `df=pd.DataFrame(np.loadtxt('path/Data.txt',delimiter=','))`
   - `np.savetxt(fname,X)`保存为txt格式fname为文件名 参数X为需要保存的函数

1. Excel
   - `pd.read_excel()`读取excel文件返回DataFrame `pandas.read_excel(io, sheet_name=0, *, header=0, names=None, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=<no_default>, date_format=None, thousands=None, decimal='.', comment=None, skipfooter=0, storage_options=None, dtype_backend=<no_default>, engine_kwargs=None)`
     - io 指定路径
     - sheet_name = 0 读取工作表名称
     - keep_default_na=True：指定是否要将默认的缺失值（例如NaN）解析为NA。
     - parse_dates=False：指定是否要解析日期。
     - decimal='.'：指定小数点字符。
   - `DataFrame.to_excel(excel_writer, *, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, inf_rep='inf', freeze_panes=None, storage_options=None, engine_kwargs=None)`写入excel `df.to_excel(excel_writer,sheet_name='sheetname',index=False)`
  
   - `excel_file = pd.ExcelFile('data.xlsx')` 加载excel文件访问多个表单

    ```python
        import pandas as pd

        # 使用 ExcelFile 加载 Excel 文件
        excel_file = pd.ExcelFile('data.xlsx')

        # 查看所有表单的名称
        print(excel_file.sheet_names)

        # 读取指定的表单
        df = excel_file.parse('Sheet1')
        print(df)

        # 关闭文件
        excel_file.close() 
     
    ```

    - ExcelWriter pandas提供的一个类 将DataFrame或Series对象写入Excel文件可以灵活控制写入过程
       - `pandas.ExcelWriter(path, engine=None, date_format=None, datetime_format=None, mode='w', storage_options=None, if_sheet_exists=None, engine_kwargs=None)`
          - path 设置写入excel路径
          - if_sheet_exists：这是一个可选参数，默认为 'error'，指定如果工作表已经存在时的行为。选项包括 'error'（抛出错误）、'new'（创建一个新工作表）、'replace'（替换现有工作表的内容）、'overlay'（在现有工作表上覆盖写入）
          - storage_options：这是一个可选参数，用于指定与存储后端连接的额外选项，例如认证信息、访问权限等，适用于写入远程存储（如 S3、GCS）

```python
#使用ExcelWriter类
import pandas as pd


# 创建一个 ExcelWriter 对象
with pd.ExcelWriter('output.xlsx') as writer:
    # df.to_excel(writer, sheet_name='Sheet1', index=False)  # 将 DataFrame 写入 Excel 文件
    # 创建 DataFrame写入多个工作表
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
```

```python
#设置日期时间格式
from datetime import date, datetime  
#使用ExcelWriter类
import pandas as pd
df = pd.DataFrame(
    [
        [date.today(), date(1999, 9, 24)],                  # 第一行：Date
        [datetime.now(), datetime(2014, 2, 28, 13, 5, 13)] # 第二行：Datetime
    ],
    index=["Date", "Datetime"],
    columns=["X", "Y"],
)
print(df)
# with pd.ExcelWriter(
#     "path_to_file.xlsx",
#     date_format="YYYY-MM-DD",
#     datetime_format="YYYY-MM-DD HH:MM:SS"
# ) as writer:
#     df.to_excel(writer)
```

```python
# 向现有文件追加
import pandas as pd

with pd.ExcelWriter("path_to_file.xlsx", mode="a", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sheet3")
```

```python
#将excel文件打包
import zipfile  
df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  
with zipfile.ZipFile("path_to_file.zip", "w") as zf:
    with zf.open("filename.xlsx", "w") as buffer:
        with pd.ExcelWriter(buffer) as writer:
            df.to_excel(writer)
```

```python
#将excel文件转换为csv文件
import pandas as pd

df = pd.read_excel("path_to_file.xlsx", sheet_name="Sheet1")
df.to_csv("output.csv", index=False)  # 将 DataFrame 导出为 CSV 文件
```

1.json

- `pd.read_json('path/json',orient = None)`从json中读取数据并加载为DataFrame
- `DataFrame.to_json()`将dataframe转换为json格式数据 `df.to_string()`用于返回DataFrame类型的数据也可以直接处理json字符串
- 还有嵌套的后面补充有点复杂

```python
import pandas as pd

df = pd.read_json(
    #path_or_buffer,      # JSON 文件路径、JSON 字符串或 URL
    orient=None,         # JSON 数据的结构方式，默认是 'columns'
    dtype=None,          # 强制指定列的数据类型
    convert_axes=True,   # 是否转换行列索引
    convert_dates=True,  # 是否将日期解析为日期类型
    keep_default_na=True # 是否保留默认的缺失值标记
)
```
