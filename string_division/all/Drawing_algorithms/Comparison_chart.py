import matplotlib.pyplot as plt

# 第一天曲线数据 C1=[97.0%, 95.0%, 97.8%,98.2%, 89.5%,76.7%]
C1 = [97.0, 95.0, 97.8, 98.2, 89.5, 76.7]

# 第二天曲线数据 C2=[100%,100%,100%, 100%, 99.6%, 95.5%]
C2 = [100, 100, 100, 100, 99.6, 95.5]

# 数据F=[10,8,6,4,2,0]
F = ['>10', '>8', '>6', '>4', '>2', '>0']

# 绘制对比折线图
plt.plot(F, C1, color='black', linestyle='--', label='Candidate itemsets before correction')  # 第一天曲线，蓝色
plt.plot(F, C2, color='black', label='Candidate itemsets after correction')   # 修正后曲线，红色
font = {'family': 'Times New Roman'}
plt.rc('font', **font)
# 设置图表标题和标签
# plt.title('匹配度对比')
plt.xlabel('Frequence')
plt.ylabel('Matching degree ratio')
plt.legend()  # 显示图例

# 显示图表
plt.show()


