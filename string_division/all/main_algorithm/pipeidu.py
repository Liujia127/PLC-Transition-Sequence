import time
start_time = time.time()
import matplotlib.pyplot as plt
from all.main_algorithm import candidate_set, frequent_items
import re


graph1= candidate_set.graph1
# 绘图
labels, values = zip(*graph1)
# 设置字体大小
plt.rcParams.update({'font.size': 13})
font = {'family': 'Times New Roman'}
plt.rc('font', **font)
# values_percent = [value / two.num * 100 for value in values]
values_percent = [value / 27 * 100 for value in values]
# 创建曲线图
# plt.figure(figsize=(10, 6))
plt.figure()
# plt.plot(labels, values_percent, marker='o', linestyle='-', color='black')
plt.bar(labels, values_percent, width=0.5, color='none', edgecolor='black', linewidth=1)
# 添加标题和标签
plt.xlabel("Parent")
plt.ylabel("Number of traces (%)")
# 旋转x轴标签以避免重叠
# plt.xticks(rotation=45)
# 在折线上显示值
for i, value in enumerate(values_percent):
    plt.text(i, value, f"{value:.1f}%", ha='center', va='bottom')
# 显示曲线图
plt.tight_layout()
plt.show()


data_length = len(frequent_items.data)
print("变迁序列的长度:", data_length)

new_list = candidate_set.cand
graph2 = []
l = len(candidate_set.cand)
# user_input = input(f"请输入一个小于{l}的整数: ")
# user_input_as_int = int(user_input)
user_input_as_int = 2

if user_input_as_int == 2:
    # 创建一个空列表来存储新的组合
    new_list = []
    # 遍历所有可能的组合
    for i in range(len(candidate_set.cand)):
        for j in range(i + 1, len(candidate_set.cand)):
            list1_key, list1_values = candidate_set.cand[i]
            list2_key, list2_values = candidate_set.cand[j]
            combined_list = f"{list1_key}+{list2_key}"  # 创建新的标识
            combined_values = list1_values + list2_values  # 合并两个列表
            new_list.append((combined_list, combined_values))
if user_input_as_int == 3:
    new_list = []
    for i in range(len(candidate_set.cand)):
        for j in range(i + 1, len(candidate_set.cand)):
            for k in range(j + 1, len(candidate_set.cand)):
                list1_key, list1_values = candidate_set.cand[i]
                list2_key, list2_values = candidate_set.cand[j]
                list3_key, list3_values = candidate_set.cand[k]
                combined_list = f"{list1_key}+{list2_key}+{list3_key}"  # 创建新的标识
                combined_values = list1_values + list2_values + list3_values  # 合并三个列表
                new_list.append((combined_list, combined_values))
if user_input_as_int == 4:
    new_list = []
    for i in range(len(candidate_set.cand)):
        for j in range(i + 1, len(candidate_set.cand)):
            for k in range(j + 1, len(candidate_set.cand)):
                for h in range(k + 1, len(candidate_set.cand)):
                    list1_key, list1_values = candidate_set.cand[i]
                    list2_key, list2_values = candidate_set.cand[j]
                    list3_key, list3_values = candidate_set.cand[k]
                    list4_key, list4_values = candidate_set.cand[h]
                    combined_list = f"{list1_key}+{list2_key}+{list3_key}+{list4_key}"  # 创建新的标识
                    combined_values = list1_values + list2_values + list3_values + list4_values  # 合并三个列表
                    new_list.append((combined_list, combined_values))
print(new_list)

# 输出新的列表，包含了所有可能的组合
for element in new_list:
    new_data = frequent_items.data
    sorted_data = sorted(element[1], key=lambda x: x[1])
    # 遍历替换element[1]中的子串
    for substring, count in sorted_data:
        new_data = new_data.replace(substring, ' ', count)  # 替换指定次数
    # 使用正则表达式删除多个连续的空白字符，然后输出划分后的字符串
    result_data = re.sub(r'\s+', ' ', new_data)


    # 统计替换后的新data的长度
    new_data = new_data.replace(' ', '')
    new_data_length = len(new_data)
    # print("替换后的新data长度:", new_data_length)
    # if new_data_length < data_length:
    if new_data_length < data_length:
        print(f"{element[0]}划分效果：{result_data}")
        # 打印一条虚线
        print('-' * 10)
        fit = data_length - new_data_length
        graph2.append((element[0], fit))
print(graph2)

# 绘图
labels, values = zip(*graph2)
# 设置字体大小
plt.rcParams.update({'font.size': 13})
font = {'family': 'Times New Roman'}
plt.rc('font', **font)
values_percent = [value / data_length * 100 for value in values]
# 创建曲线图
plt.figure()
# plt.plot(labels, values_percent, marker='o', linestyle='-', color='black')
plt.bar(labels, values_percent, width=0.5, color='none', edgecolor='black', linewidth=1)  # 不填充颜色，仅显示边框
# 添加标题和标签
plt.xlabel("Parent")
plt.ylabel("Length of sequence (%)")
# 旋转x轴标签以避免重叠
# plt.xticks(rotation=45)
# 在折线上显示值
for i, value in enumerate(values_percent):
    plt.text(i, value, f"{value:.1f}%", ha='center', va='bottom')
# 显示曲线图
plt.tight_layout()
plt.show()


# 在这里运行你的代码

end_time = time.time()
execution_time = end_time - start_time
print(f"代码运行时间为: {execution_time} 秒")
