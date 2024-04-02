import random
from all.data_processing import one

# 统计轨迹总数
num = 0
user_input = input("选取的轨迹概率> ")
sel_fre = int(user_input)
# sel_fre = 0
new_output_count = {}
# 调整需要的轨迹，以及频次
for combined_event_value, count in one.output_count.items():
    # if count > (num // 100):
    if count > sel_fre :
        num = num + count//1
        new_output_count[combined_event_value] = count // 1   # 更新count   count // 10

# for combined_event_value, count in new_output_count.items():
#     print(f"轨迹 '{combined_event_value}'  {count} 次")
print(f"轨迹总数：{num}")


A = []
print(new_output_count)
# new_output_count={'ae': 121, 'aie': 363, 'bhfcgd': 193, 'bhcfgd': 89, 'bhcgfd': 80, 'bhfc': 64, 'bhcf': 90}
for string, count in new_output_count.items():
    A.extend([string] * count)

random.shuffle(A)
transition_seq = ''.join(A)
print(f"变迁序列：{transition_seq}")
