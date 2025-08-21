---
title: 'DataVisualization03'
date: 2025-08-19T15:24:39+09:00
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

## Matplotlib与Seaborn绘图

- 使用matplotlib 和 seaborn `import matplotlib.pyplot as plt` `import seaborn as sns`
- 理解各个元素的使用和调用
- 绘制折线图 绘制直方图

-------

### Maplotlib

1. 基础类(primitives) : 点plot 线line 文字text 图legend 网格grid 标题title 图片image
1. 容器(containers) : 图形figure 坐标图形axes 坐标轴axis 刻度tick

- 基础类是我们需要绘制的标准对象 容器元素则包含基础类元素组成整体
- figure &rarr axes &rarr axis &rarr tick
  - figure对象 整个图形 至少包含一个子图(axes对象) 包含图名(title)图例(legend)
  - axes对象 子图对象 绘制多个子图时需要
  - axis对象 鼠标周对象 有locator和formatter两个子对象控制刻度位置和显示数值
  - tick对象 坐标轴包含两个元素 刻度(包含刻度本身和刻度标签) 标签(坐标轴标签)
- `plt.style.available`查看可用样式
- 对图进行细微的调整需要获取 axes对象及其子对象 和 figure对象
  - `plt.gca()`返回当前状态下的axes对象
  - `plt.gca().get_children()`查看当前axes对象下的元素
  - `plt.gcf()`返回当前状态下的的figure对象 用于遍历多个图形的axes对象

- 图表主要元素

    | 函数                        | 参数                                                                                  | 功能                 |
    |-----------------------------|---------------------------------------------------------------------------------------|----------------------|
    | `plt.figure()`              | figsize(图标尺寸) dpi                                                                 | 设置图标大小和分辨率 |
    | `title()`                   | str(图名),fontdict(文本格式字体大小等)                                                | 设置标题             |
    | `xlabel()` `ylabel()`       | xlabel(x轴名)   ylabel(y轴名)                                                         | 设置x轴y轴标题       |
    | `axis()` `xlim()`  `ylim()` | xmin,xmax,ymin,ymax                                                                   | 设置范围             |
    | `xticks()` `yticks()`       | ticks(刻度数值) lables(刻度名称) fontdict                                             | 设置x轴y轴刻度       |
    | `grid()`                    | b(网格线) which(主次网格线)axis(x轴y轴网格线) color linestyle linewidth alpha(透明度) | 设置x轴y轴格式       |
    | `legend()`                  | loc(位置) edgecolor facecolor fontsize                                                | 控制图例显示         |

- 图表类型

  | 函数                                   | 参数                                                                                                                                                                                  | 功能              |
  |----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
  | `plt.plot(x, y, '[颜色][标记][线条]')` | x y color(线条颜色) linestyle marker markeredgecolor(标记框颜色) markeredgewidth(标记框宽度) markersize,lable(线条标签)                                                               | 折线图            |
  | `plt.scatter()`                        | x y s(散点大小) label marker linewidths(散点边框宽度) edgecolors(边框颜色)                                                                                                            | 散点图 气泡图     |
  | `plt.bar()`                            | x height(柱形高度) width(柱形宽度) align(柱形位置) color edgecolor linewidth(柱形边框宽度)                                                                                            | 柱形图堆积图      |
  | `barh`                                 | x height(柱形高度) width(柱形宽度) align(柱形位置) color edgecolor linewidth(柱形边框宽度)                                                                                            | 条形图 堆积条形图 |
  | `errorbar()`                           | x y yerr(y轴误差范围) xerr fmt(数据点的标记和连接方式) elinewidth(误差棒宽度) ms(数据点大小) mfc(数据点填充色) mec(数据点标记边缘颜色) capthick(误差棒横杠的粗细) capsize(误差棒大小) | 误差棒            |
  | `hist()`                               | x bins(箱的总数) range(统计范围) density(是否为统计频率) align color label                                                                                                            | 统计直方图        |

```python
import matplotlib.pyplot as plt
plt.figure(1)  # 第1个图
plt.plot([1,2,3], [1,2,3])

plt.figure(2)  # 第2个图
plt.plot([1,2,3], [1,4,9])

plt.show()
```

- 绘图流程:
  - 确定数据
  - 先使用`plt.figure()`设置大小和分辨率和窗口数量
  - 确定图名 坐标轴名称  
  - 选择对应函数绘制相关图 网格设置之类的
  - `plt.show()`

```python
#grid(color = 'color', linestyle = 'linestyle', linewidth = number)
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid(color = 'g', linestyle = '-', linewidth = 0.5)

plt.show()
```

- 绘制多图
  - `subplot()` 和 `subplots()`方法来绘制多个子图
  - 注意`subplot`在绘图时需要指定位置 `subplots()`可以生成多个

``` python
subplot(nrows, ncols, index, **kwargs)
subplot(pos, **kwargs)
subplot(**kwargs)
subplot(ax)
```

- 将绘图区域分成nows行和ncol列 从左至右从上至下进行编号左上为1右下为N 编号通过index设置
- 比如将numRows = 1 numCols = 2 就是绘制成1*2的图片区域对应坐标 为(1,1) (1,2)

```python
import matplotlib.pyplot as plt
import numpy as np

#plot 1
xpoints = np.array([0,10])
ypoints = np.array([0,100])

plt.subplot(1,2,1)
plt.plot(xpoints,ypoints)

plt.title("Subplot 1")
#plot 2
xpoints = np.array([0,20])
ypoints = np.array([100,200])
plt.subplot(1,2,2)
plt.plot(xpoints,ypoints)

plt.title("Subplot 2")

plt.suptitle("Main Title")
plt.show()
```

- subplots()使用:
  - `matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)`
  - 创建的是一个figure对象和axes对象两个
  - nrows: 默认为1 设置图表的行数
  - ncols: 默认为1 设置图标的列数
  - sharex,sharey 设置x，y是否共享默认为false 可以设置为`none`,`all`,`row`,`col`False和None每个子图的x轴和y轴都是独立的 True或all所有子图共享x或y轴 `row`设置每个子图行共享一个x或y轴 `col`设置每个子图列共享一个x或y轴
  - squeeze: 布尔值 表示额外的维度从返回的Axes对象中挤出对于 N*1 或 1*N 个子图，返回一个 1 维数组，对于 N*M，N>1 和 M>1 返回一个 2 维数组。如果设置为 False，则不进行挤压操作，返回一个元素为 Axes 实例的2维数组，即使它最终是1x1
  - subplot_kw：可选，字典类型。把字典的关键字传递给 add_subplot() 来创建每个子图。
  - gridspec_kw：可选，字典类型。把字典的关键字传递给 GridSpec 构造函数创建子图放在网格里(grid)。
  - **fig_kw：把详细的关键字参数传给 figure() 函数。

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一些测试数据 -- 图1
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# 创建一个画像和子图 -- 图2
fig, ax = plt.subplots() 
ax.plot(x, y)
ax.set_title('Simple plot')

# 创建两个子图 -- 图3
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# 创建四个子图 -- 图4
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# 共享 x 轴
plt.subplots(2, 2, sharex='col')

# 共享 y 轴
plt.subplots(2, 2, sharey='row')

# 共享 x 轴和 y 轴
plt.subplots(2, 2, sharex='all', sharey='all')

# 这个也是共享 x 轴和 y 轴
plt.subplots(2, 2, sharex=True, sharey=True)

# 创建标识为 10 的图，已经存在的则删除
fig, ax = plt.subplots(num=10, clear=True)

plt.show()
```

- 柱形图实例
  - `matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)`

- 保存图像
- `plt.savefig('filename.pdf',format=pdf)`要在plt.show()之前使用 支持pdf,png,jpg,svg等
- `matplotlib.pyplot.imsave(fname, arr, **kwargs)`

```python
# 获取系统字体列表
from matplotlib import pyplot as plt
import matplotlib
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)
```

```python
import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体
plt.rcParams['font.family'] = 'WenQuanYi Micro Hei'  # 设置中文字体为黑体

x = np.array(["a", "b", "c", "d"])
y = np.array([12, 22, 6, 18])
plt.title('柱状图示例')

plt.bar(x,y,color
        ='blue',width=0.5)
plt.show()
```

### seaborn使用

- 建立在matplolib上的数据可视化库
- 简化数据可视化过程提供主题

|函数|参数说明 |类型 |
|---|---|---|
|sns.lineplot()| x y hue(颜色映射) size(线条宽度映射) style(线条宽度类型映射) data(数据框格式的数据) palette(颜色模版) sizes(线条宽度) markers(数据标记类型)|折线图 |
|sns.scatterplot()|x y hue(颜色映射) size style(数据标记类型映射) data(DataFrame格式的数据) palette(颜色模版) sizes(数据标记大小) markers(数据标记类型)|散点图|
|sns.barplot()|x y hue data order(X轴的显示顺序) orient palette color size errcolor（误差棒颜色） errwidth capsize（误差棒大小） dogde（数据是否分离显示）|带误差棒的柱形图|

- 图表风格
  - 主题和调色  `sns.set_theme(style="whitegrid", palette="pastel")` 默认`darkgrid` 深色网格 `dark` 深色 `whitegrid` `white` `tocls`
  - 模板 `sns.set_theme(context="paper")` paper notebook talk poster
  - `sns.set_theme(style="white", palette="pastel",context="notebook")`

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 设置主题和颜色调色板
sns.set_theme(style="white", palette="pastel",context="notebook")
# 示例数据
products = ["Product A", "Product B", "Product C", "Product D"]
sales = [120, 210, 150, 180]

# 创建柱状图
sns.barplot(x=products, y=sales)

# 添加标签和标题
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales by Category")

# 显示图表
plt.show()
```
