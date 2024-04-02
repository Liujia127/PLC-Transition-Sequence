from all.data_processing import two
from all.main_algorithm import candidate_set, frequent_items, pipeidu
import importlib
import matplotlib.pyplot as plt

# 准备一个列表来存储六组数据
graph1_list = []
graph2_list = []
n =[]
l =[]

num = two.num
n.append(num)
length = len(two.transition_seq)
l.append(length)
graph1 = candidate_set.graph1
length = two.transition_seq
graph1_list.append(graph1)
graph2 = pipeidu.graph2
graph2_list.append(graph2)

for i in range(5):
    two = importlib.reload(two)
    frequent_items = importlib.reload(frequent_items)
    candidate_set = importlib.reload(candidate_set)
    pipeidu = importlib.reload(pipeidu)
    num = two.num
    n.append(num)
    length = len(two.transition_seq)
    l.append(length)
    graph1 = candidate_set.graph
    graph1_list.append(graph1)
    graph2 = pipeidu.graph
    graph2_list.append(graph2)


# 创建大图
fig, axes = plt.subplots(2, 3,  sharey=True)  # 2行3列的子图布局
fig2, axes2 = plt.subplots(2, 3,  sharey=True)  # 第二个大图，2行3列的子图布局

# 在每个子图中绘制数据
for i, ax in enumerate(axes.flat):
    data = graph1_list[i]
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]
    y_values_percent = [int(y_value) / int(n[i]) * 100 for y_value in y_values]
    ax.plot(x_values, y_values_percent, marker='o', linestyle='-', color='b')
    # 设置字体大小
    plt.rcParams.update({'font.size': 10})
    font = {'family': 'SimHei'}
    plt.rc('font', **font)
    # 在折线上显示值
    for j, value in enumerate(y_values_percent):
        ax.text(x_values[j], value, f"{value:.1f}%", ha='center', va='bottom')
    # 添加注释到右上角
    annotation_text = f"sel_fre>{10-i * 2}"
    ax.annotate(annotation_text, xy=(0.95, 0.95), xycoords='axes fraction', ha='right', va='top')

for i, ax in enumerate(axes2.flat):
    data = graph2_list[i]
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]
    y_values_percent = [int(y_value) / int(l[i]) * 100 for y_value in y_values]
    ax.plot(x_values, y_values_percent, marker='o', linestyle='-', color='b')
    # 设置字体大小
    plt.rcParams.update({'font.size': 10})
    font = {'family': 'SimHei'}
    plt.rc('font', **font)
    # 在折线上显示值
    for j, value in enumerate(y_values_percent):
        ax.text(x_values[j], value, f"{value:.1f}%", ha='center', va='bottom')
    # 添加注释到右上角
    annotation_text = f"sel_fre>{10-i * 2}"
    ax.annotate(annotation_text, xy=(0.95, 0.95), xycoords='axes fraction', ha='right', va='top')

fig.suptitle("Track-number ratio", fontsize=16)
fig.text(0.5, 0.04, "Parent", ha="center", fontsize=14)
fig.text(0.04, 0.5, "Number of tracks (%)", va="center", rotation="vertical", fontsize=14)
fig2.suptitle("Matched-degree", fontsize=16)
fig2.text(0.5, 0.04, "Parent", ha="center", fontsize=14)
fig2.text(0.04, 0.5, "Length of sequence (%)", va="center", rotation="vertical", fontsize=14)

plt.tight_layout()
plt.tight_layout()
plt.show()
