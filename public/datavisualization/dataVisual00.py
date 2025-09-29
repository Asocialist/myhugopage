# # import matplotlib.pyplot as plt

# # squares = [1, 4, 9, 16, 25]
# # plt.plot(squares)
# # plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt

# # 创建一个 DataFrame
# sales_data = {'月份': ['一月', '二月', '三月', '四月'],
#               '销售额': [150, 220, 180, 270]}
# df = pd.DataFrame(sales_data).set_index('月份')
# # Pandas 自动使用索引作为 X 轴，列名作为图例，列数据作为 Y 轴
# ax = df.plot(kind='line', title='月度销售额')
# plt.show() # 最终显示图像仍然需要 matplotlib.pyplot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # 1. 导入 seaborn

# --- 设置 Seaborn 的主题 ---
# 这会改变 Matplotlib 的默认参数，让图表更好看
sns.set_theme(style="darkgrid", font="WenQuanYi Micro Hei") # 2. 设置主题和中文字体

# --- 后续代码完全不变 ---
sales_data = {'月份': ['一月', '二月', '三月', '四月'],
              '销售额': [150, 220, 180, 270]}
df = pd.DataFrame(sales_data).set_index('月份')

# 即使是调用 Pandas 的 .plot()，也会应用 Seaborn 的风格
ax = df.plot(kind='line', title='月度销售额', marker='o') 
ax.set_ylabel("销售额 (万元)")
plt.show()