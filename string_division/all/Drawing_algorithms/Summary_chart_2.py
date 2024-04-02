import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter

graph1_list = [[('j', 482), ('c', 306), ('g', 349), ('h', 316), ('l', 334), ('d', 190), ('m', 250), ('f', 28), ('k', 68)],
               [('j', 482), ('c', 306), ('g', 304), ('h', 286), ('l', 328), ('d', 314), ('m', 280), ('b', 12), ('f', 100), ('k', 122)],
               [('d', 296), ('j', 482), ('c', 306), ('g', 258), ('h', 272), ('l', 336), ('m', 320), ('b', 11), ('f', 88), ('k', 138)],
               [('d', 378), ('j', 482), ('c', 306), ('g', 310), ('h', 293), ('l', 328), ('m', 345), ('b', 64), ('f', 88), ('k', 149), ('n', 5), ('i', 5), ('e', 6)],
               [('d', 459), ('j', 482), ('c', 306), ('g', 307), ('h', 185), ('l', 355), ('m', 326), ('b', 61), ('f', 195), ('k', 192), ('n', 61), ('i', 29), ('e', 3)],
               [('n', 848), ('m', 428), ('b', 174), ('f', 208), ('k', 268), ('e', 440), ('j', 482), ('c', 306), ('g', 254), ('h', 284), ('l', 295), ('i', 122)]]
graph2_list = [[('j+c', 2892), ('j+d', 3527), ('j+m', 4370), ('j+f', 3004), ('j+k', 3232), ('g+m', 3274), ('h+m', 3226), ('l+d', 2803), ('l+m', 3482)],
               [('j+d', 4032), ('j+m', 4640), ('j+b', 2964), ('j+f', 3409), ('j+k', 3580), ('g+d', 2961), ('g+m', 3391), ('h+d', 2937), ('h+m', 3338), ('l+d', 3247), ('l+m', 3716)],
               [('d+j', 3948), ('d+l', 3387), ('j+m', 5005), ('j+f', 3377), ('j+k', 3687), ('g+m', 3536), ('h+m', 3593), ('l+m', 4129)],
               [('d+j', 4264), ('d+g', 3377), ('d+h', 3429), ('d+l', 3809), ('j+m', 5265), ('j+f', 3429), ('j+k', 3760), ('c+m', 3291), ('g+m', 3965), ('h+m', 3917), ('l+m', 4341)],
               [('d+j', 4506), ('d+g', 3648), ('d+l', 4059), ('j+m', 5071), ('j+b', 3245), ('j+f', 3799), ('j+k', 3941), ('g+m', 3789), ('l+m', 4217), ('l+f', 3438), ('l+k', 3514)],
               [('n+m', 5569), ('n+b', 5199), ('n+f', 5303), ('n+k', 5563), ('n+j', 6325), ('n+c', 5317), ('n+g', 5620), ('n+h', 5634), ('n+l', 5756), ('n+i', 5106), ('m+j', 6434), ('m+h', 5063), ('m+l', 5158)]]
num =[749, 789, 812, 837, 859, 1000]
length =[4506, 4886, 5115, 5360, 5665, 8389]

# 创建大图
fig, axes = plt.subplots(2, 3,  sharey=True)  # 2行3列的子图布局
fig2, axes2 = plt.subplots(2, 3,  sharey=True)  # 第二个大图，2行3列的子图布局

# 在每个子图中绘制数据
for i, ax in enumerate(axes.flat):
    data = graph1_list[i]
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]
    y_values_percent = [int(y_value) / int(num[i]) * 100 for y_value in y_values]
    ax.plot(x_values, y_values_percent,  linestyle='-', color='black', linewidth=1.0)
    # 设置字体大小
    plt.rcParams.update({'font.size': 13})
    font = {'family': 'Times New Roman'}
    plt.rc('font', **font)
    # 在折线上显示值
    # for j, value in enumerate(y_values_percent):
    #     ax.text(x_values[j], value, f"{value:.1f}%", ha='center', va='bottom')
    # 添加注释到右上角
    annotation_text = f"fre>{10-i * 2}"
    ax.annotate(annotation_text, xy=(0.95, 0.95), xycoords='axes fraction', ha='right', va='top')

for i, ax in enumerate(axes2.flat):
    data = graph2_list[i]
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]
    y_values_percent = [int(y_value) / int(length[i]) * 100 for y_value in y_values]
    ax.plot(x_values, y_values_percent, linestyle='-', color='black', linewidth=1.0)
    # 设置字体大小
    plt.rcParams.update({'font.size': 13})
    font = {'family': 'Times New Roman'}
    plt.rc('font', **font)
    ax.set_xticks(range(len(x_values)))  # 设置x轴刻度
    ax.set_xticklabels(x_values, rotation=90)  # 设置x轴刻度标签，并旋转
    ax.xaxis.set_major_locator(FixedLocator(range(len(x_values))))  # 确保与FixedFormatter一起使用FixedLocator
    # 在折线上显示值
    # for j, value in enumerate(y_values_percent):
    #     ax.text(x_values[j], value, f"{value:.1f}%", ha='center', va='bottom')
    # 添加注释到右上角
    annotation_text = f"fre>{10-i * 2}"
    ax.annotate(annotation_text, xy=(0.95, 0.95), xycoords='axes fraction', ha='right', va='top')

# fig.suptitle("Trace number ratio", fontsize=16)
fig.text(0.5, 0.02, "Parent", ha="center", fontsize=13)
fig.text(0.02, 0.5, "Trace number ratio (%)", va="center", rotation="vertical", fontsize=13)
# fig2.suptitle("Matching degree ratio", fontsize=16)
fig2.text(0.5, 0.02, "Parent", ha="center", fontsize=13)
fig2.text(0.02, 0.5, "Matching degree ratio (%)", va="center", rotation="vertical", fontsize=13)

plt.tight_layout()
plt.tight_layout()
plt.show()