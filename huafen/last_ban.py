import two
# 构建了输入字符串 `input_string` 的后缀数组，并返回一个包含后缀索引的列表
def build_suffix_array(input_string):
    suffixes = [(input_string[i:], i) for i in range(len(input_string))]
    suffixes.sort()
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def find_sorted_substrings(input_string):
    suffix_array = build_suffix_array(input_string)
    substr_freq = {}  # 用于存储子串频率的字典

    for i in range(len(suffix_array)):
        suffix = input_string[suffix_array[i]:]
        for j in range(2, len(suffix) + 1):  # 从长度为2的子串开始
            substring = suffix[:j]
            if substring in substr_freq:
                substr_freq[substring] += 1
            else:
                substr_freq[substring] = 1

    # 按频率高低排序，并只保留频率和长度大于等于2的子串
    sorted_substrings = [(substring, freq) for substring, freq in substr_freq.items() if freq >= 2]
    sorted_substrings.sort(key=lambda x: (-x[1], x[0]))  # 按频率降序排序，相同频率按字典序升序排序

    # 删除被其他子串包含且频率相同的较短子串
    result = []
    for substring, freq in sorted_substrings:
        is_contained = False
        for other_substring, other_freq in sorted_substrings:
            if substring != other_substring and substring in other_substring and freq == other_freq:
                is_contained = True
                break
        if not is_contained:
            result.append((substring, freq))

    return result

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # 构建部分匹配表
    prefix_table = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j

    # 开始匹配
    j = 0
    max_length = 0
    max_repeat = ""
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j > max_length:
            max_length = j
            max_repeat = pattern[:j]

    return max_repeat

def find_max_non_overlapping_repeats(text):
    n = len(text)
    max_length = 0
    longest_repeat = ""

    for window_size in range(2, n // 2 + 1):
        for start in range(n - window_size + 1):
            window = text[start:start + window_size]
            for i in range(start + 1, n - window_size + 1):
                if window == text[i:i + window_size]:
                    if window_size > max_length:
                        max_length = window_size
                        longest_repeat = window
                    break

    return longest_repeat

def remove_contained_substrings(children):
    i = 0
    while i < len(children) - 1:
        j = i + 1
        while j < len(children):
            if children[i] in children[j]:
                children.pop(i)
                break
            j += 1
        else:
            i += 1

# 示例
input_str2 = "abcdeafghidjkleafgcmdnkoeafgcijdkleafghidjkleafghmndkoeafghmndkoeafgcmndkoeafghidjkleafghmndkoeafghmndkoeafgcmndkoeafghijdkleafgcmdnkoeafghijdkleafgcmndkoeafgcijdkleafghijdkleafghmndkoeafghmndkoeafgcmndkoeafghijdkleafghmndkoeafghmdnkoeafgcmndkoeafghijdkleafgcmndkoeafghijdkleafgcmdnkoeafgcijdkl"

result = find_sorted_substrings(input_str2)
result_set = [substring for substring, _ in result]

# 修改后的代码
def has_partial_overlap(array1, string2):
    for string in array1:
        l = min(len(string), len(string2))
        for i in range(l):
            if string[-(i + 1):] == string2[:i + 1]:
                return False
    return True

def optimize_string_partition(array1, string2):
    i = 0
    array2 = []
    while i < len(string2):
        found = False
        for substring in array1:
            if string2[i:i + len(substring)] == substring:
                array2.append(substring)
                i += len(substring)
                found = True
                break
        if not found:
            array2.append(string2[i])
            i += 1
    return array2

# A = []
# A.append(result_set[0])  # 将频率最高的子串加入数组A
# result_set.pop(0)  # 从result_set中移除已选择的子串
#
# while result_set:
#     new_substring = result_set[0]
#     if has_partial_overlap(A, new_substring):
#         A.append(new_substring)  # 加入数组A
#         result_set.pop(0)  # 从result_set中移除已选择的子串
#     else:
#         result_set.pop(0)  # 如果不符合条件，从result_set中移除该子串
#
# B = optimize_string_partition(A, input_str2)
# D = []
# E = []
# for i in range(len(B) - 1):
#     if (len(B[i]) != 1 and len(B[i + 1]) == 1) or (len(B[i]) == 1 and len(B[i + 1]) != 1):
#         combined_str = B[i] + B[i + 1]
#         if (combined_str in result_set) and (combined_str not in D):
#             for j in range(len(A)):
#                 if len(B[i+1]) == 1:
#                     if A[j] == B[i]:
#                         D.append(combined_str)
#                         if A[j] not in E:
#                             E.append(A[j])
#                 else:
#                     if A[j] == B[i + 1]:
#                         D.append(combined_str)
#                         if A[j] not in E:
#                            E.append(A[j])
# for string in A:
#     if string not in E:
#         D.append(string)
#
# B = optimize_string_partition(D, input_str2)
# print(B)
