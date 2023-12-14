class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0

def insert_into_trie(root, string):
    node = root
    for char in string:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.freq += 1

def find_sorted_substrings(input_string):
    root = TrieNode()
    n = len(input_string)

    # 从后缀数组中逆序遍历后缀并插入到 Trie 树中
    for i in range(n - 1, -1, -1):
        suffix = input_string[i:]
        if len(suffix) > 1:  # 仅考虑长度大于1的后缀
            insert_into_trie(root, suffix)

    # 使用迭代方式遍历 Trie 树以获取所有出现频率大于等于2的子串
    def find_substring_frequent(node, prefix):
        result = []
        stack = [(node, prefix)]
        while stack:
            current_node, current_prefix = stack.pop()
            if len(current_prefix) > 1 and current_node.freq >= 2:
                result.append((current_prefix, current_node.freq))
            for char, child in current_node.children.items():
                stack.append((child, current_prefix + char))
        return result

    substring_frequent = find_substring_frequent(root, "")

    # 按频率排序
    substring_frequent.sort(key=lambda x: x[1], reverse=True)

    # 删除被其他子串包含且频率相同的较短子串
    final_result = []
    for substring, freq in substring_frequent:
        is_contained = False
        for other_substring, other_freq in substring_frequent:
            if substring != other_substring and substring in other_substring and freq == other_freq:
                is_contained = True
                break
        if not is_contained:
            final_result.append((substring, freq))

    return final_result

# 将子串组织成父串和子串的关系，其中父串是子串的前缀
def group_substrings(result_set):
    substring_groups = {}   # 用于存储子串和父串的关系

    for substring in result_set:
        for parent in substring_groups:
            if substring.startswith(parent):
                substring_groups[parent].append(substring)
                break
        else:
            substring_groups[substring] = []

    return substring_groups

# 将子串组织成父串和子串的关系，其中父串是子串的前缀
def group_substrings(result_set):
    substring_groups = {}  # 用于存储子串和父串的关系

    for substring in result_set:
        found_parent = False
        for parent, children in substring_groups.items():
            if substring.startswith(parent):
                children.append(substring)
                found_parent = True
                break
        if not found_parent:
            substring_groups[substring] = []

    return substring_groups

# 删除被其他子串包含的子串
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

# KMP算法，用于在文本 `text` 中查找模式串 `pattern` 的最长重复子串
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

# 在文本 `text` 中查找不重叠的最长重复子串
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


# 比较两个数组是否相等
def compare_arrays(arr1, arr2):
    return arr1 == arr2

# 判断数组是否有尾部重复
def has_partial_overlap(array1, string2):
    for string in array1:
        l = min(len(string), len(string2))
        for i in range(l):
            if string[-(i + 1):] == string2[:i + 1]:
                return False
    return True

# 用数组中的频繁项分割长字符串
def partition(array1, string1):
    i = 0
    array2 = []
    while i < len(string1):
        found = False
        for substring in array1:
            if input_str2[i:i + len(substring)] == substring:
                array2.append(substring)
                i += len(substring)
                found = True
                break
        if not found:
            # 如果没有找到匹配的子串，将当前字符单独添加到B中
            array2.append(input_str2[i])
            i += 1
    return array2



# 打开文件以读取数据
with open('one_string.txt', 'r') as file:
    data_as_string = file.read()


input_str3 = "acbcbdbcbd"
input_str2 = "abcdeafghidjkleafgcmdnkoeafgcijdkleafghidjkleafghmndkoeafghmndkoeafgcmndkoeafghidjkleafghmndkoeafghmndkoeafgcmndkoeafghijdkleafgcmdnkoeafghijdkleafgcmndkoeafgcijdkleafghijdkleafghmndkoeafghmndkoeafgcmndkoeafghijdkleafghmndkoeafghmdnkoeafgcmndkoeafghijdkleafgcmndkoeafghijdkleafgcmdnkoeafgcijdkl"
input_str1 = "aclbpjaclbpjaclbpjaclbpjaclbpjaclbpjaclbpjaclbpjaclbpjaclbpjaclbpjaclbpjacdkclbphacdkclbphacdkclbphacdkclbphaclbgobphaclbgobphaclbgobphaclbiobpjaclbiobpjaclbiobpjacmefnkclbpjacmefnkclbpjacmefnkclbpjaclbiobiobpjacdkclbgobpjaclbgobgobpjaclbgobgobpjacdkcmefnkclbpjaclbiobiobphaclbphaclbphaclbphaclbphaclbphaclbphaclbphaclbphacdkclbpjacdkclbpjacdkclbpjacdkclbpjacdkcdkclbphaclbiobphaclbiobphaclbiobphaclbgobiobpjacdkclbiobgobphacmefnkclbphacmfenkclbgobphacdkclbiobphaclbgobpjaclbgobpjaclbgobpjacmfenkcdkclbpjaclbgobgobphaclbiobgobpj"
result = find_sorted_substrings(input_str1)
result_set = []
for substring, freq in result:
    print(f"Substring: '{substring}', Frequency: {freq}")
    result_set.append(substring)

substring_groups = group_substrings(result_set)
print(result_set)
# 打印划分后的组
i = 0
candidate_sum = []
for parent, children in substring_groups.items():
    candidate_sets = []
    # print(f"Parent: '{parent}', Children: {children}")
    if len(children) > 1:
        children.sort()
        remove_contained_substrings(children)
    print(f"Parent: '{parent}', 新的Children:", children)
    candidate_sets.append(parent)
    for string in children:
        max_repeat = find_max_non_overlapping_repeats(string)
        if len(max_repeat) > 0:
            if max_repeat not in candidate_sets:
                candidate_sets.append(max_repeat)
    print(candidate_sets)
    flag = 0
    pre = []
    cur = []
    next = []
    if len(candidate_sets) > 1:
        while flag == 0:
            candidate_sets.sort()
            remove_contained_substrings(candidate_sets)
            pre = candidate_sets
            for string in candidate_sets:
                cur = find_max_non_overlapping_repeats(string)
                if len(cur) > 0:
                    if cur not in candidate_sets:
                        next.append(cur)
                else:
                    next.append(string)
            candidate_sets = next
            flag = compare_arrays(pre, next)
            if len(pre) == 1:
                flag = 1
            next = []
    if len(pre) >= 1:
        candidate_sets = pre
    i = i + 1
    for string in candidate_sets:
        candidate_sum.append(string)
    print(f"Candidate_sets_{i}:{candidate_sets}")
print(f"Candidates:{candidate_sum}")
print(result)

can_fre = []
for string in candidate_sum:
    for substring, freq in result:
        if string == substring:
            can_fre.append((substring, freq))
can_fre.sort(key=lambda x: x[1], reverse=True)  # 按频率降序排序
print(can_fre)
# 从can_fre选择频率最高的子串加入数组A
A = []
A.append(can_fre[0][0])  # 将频率最高的子串加入数组A
can_fre.pop(0)  # 从can_fre中移除已选择的子串


# 从can_fre选择一个子串，与之前所有子串的尾部都不重复，加入数组A
while can_fre:
    new_substring, freq = can_fre[0]
    if has_partial_overlap(A, new_substring):
        A.append(new_substring)  # 加入数组A
        can_fre.pop(0)  # 从can_fre中移除已选择的子串
    else:
        can_fre.pop(0)  # 如果不符合条件，从can_fre中移除该子串
print(A)



# B = partition(A, input_str2)
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
# print(B)
# # print(A)
# print(D)
# B = partition(D, input_str2)
# print(B)
