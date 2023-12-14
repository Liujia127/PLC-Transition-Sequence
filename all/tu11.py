import matplotlib.pyplot as plt

# 第一天曲线数据 C1=[97.0%, 95.0%, 97.8%,98.2%, 89.5%,76.7%]
C1 = [97.0, 95.0, 97.8, 98.2, 89.5, 76.7]

# 第二天曲线数据 C2=[100%,100%,100%, 100%, 99.6%, 95.5%]
C2 = [100, 100, 100, 100, 99.6, 95.5]

# 数据F=[10,8,6,4,2,0]
F = ['>10', '>8', '>6', '>4', '>2', '>0']

# 绘制对比折线图
plt.plot(F, C1, color='blue', label='修正前的候选项集')  # 第一天曲线，蓝色
plt.plot(F, C2, color='red', label='修正后的候选项集')   # 修正后曲线，红色
font = {'family': 'SimHei'}
plt.rc('font', **font)
# 设置图表标题和标签
# plt.title('匹配度对比')
plt.xlabel('Frequence')
plt.ylabel('Matched-degree')
plt.legend()  # 显示图例

# 显示图表
plt.show()
