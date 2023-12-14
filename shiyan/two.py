import random
import one

# 定义字符串及对应出现次数的集合
string_data = one.output_count
# A = []
# B = []
C = []

# 实验1
# for string, count in string_data.items():
#     A.extend([string] * count)

# 实验3
for string, count in string_data.items():
    C.extend([string] * count)
random.shuffle(C)

# 实验2
# while any(count > 0 for string, count in string_data.items()):
#     string_data_list = list(string_data.items())  # 将字典转换为列表以便排序
#     string_data_list.sort(key=lambda x: x[1], reverse=True)  # 按频率降序排序
#     for i, (string, count) in enumerate(string_data_list):
#         if count > 0:
#             B.append(string)
#             string_data[string] = count - 1

# 连接字符串
# result_string1 = ''.join(A)
# result_string2 = ''.join(B)
result_string3 = ''.join(C)

# 输出最终字符串
# print(result_string1)
# print(result_string2)
print(result_string3)
