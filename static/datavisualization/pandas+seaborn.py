import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks", font="WenQuanYi Micro Hei")

# 准备更复杂的数据
sales_data_multi = {
    '月份': ['一月', '二月', '三月', '四月', '一月', '二月', '三月', '四月'],
    '区域': ['华北', '华北', '华北', '华北', '华南', '华南', '华南', '华南'],
    '销售额': [150, 220, 180, 270, 130, 240, 200, 250]
}
df_multi = pd.DataFrame(sales_data_multi)

plt.figure(figsize=(10, 6)) # 可以用 Matplotlib 来设置画布大小

# 使用 Seaborn 的 barplot 函数
# - data=df_multi: 直接传入整个 DataFrame
# - x='月份', y='销售额': 用列名字符串指定 x 和 y 轴
# - hue='区域': 将“区域”列映射到颜色，自动分组并生成图例
ax = sns.barplot(data=df_multi, x='月份', y='销售额', hue='区域')

# 最后，仍然可以用 Matplotlib 的方法进行微调
ax.set_title('各区域月度销售额对比', fontsize=16)
ax.set_ylabel('销售额 (万元)')
ax.set_xlabel('月份')

plt.show()