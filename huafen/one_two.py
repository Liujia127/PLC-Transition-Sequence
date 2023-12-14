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
    def find_frequent_substrings(node, prefix):
        result = []
        stack = [(node, prefix)]
        while stack:
            current_node, current_prefix = stack.pop()
            if len(current_prefix) > 1 and current_node.freq >= 2:
                result.append((current_prefix, current_node.freq))
            for char, child in current_node.children.items():
                stack.append((child, current_prefix + char))
        return result

    frequent_substrings = find_frequent_substrings(root, "")

    # 按频率排序
    frequent_substrings.sort(key=lambda x: x[1], reverse=True)

    # 删除被其他子串包含且频率相同的较短子串
    final_result = []
    for substring, freq in frequent_substrings:
        is_contained = False
        for other_substring, other_freq in frequent_substrings:
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
        j += (pattern[i] == pattern[j])
        prefix_table[i] = j

    # 开始匹配
    j = 0
    max_length = 0
    max_repeat = ""

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        j += (text[i] == pattern[j])

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

# 生成简化后的候选项集
def candidate_sets(substring_groups):
    i = 0
    candidate_sum = []
    for parent, children in substring_groups.items():
        candidate_sets = []
        print(f"Parent: '{parent}', Children: {children}")

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
    return candidate_sum

# 打开文件以读取数据
with open('one_string.txt', 'r') as file:
    data_as_string = file.read()

result = find_sorted_substrings(data_as_string)
result_set = []
for substring, freq in result:
    # print(f"Substring: '{substring}', Frequency: {freq}")
    result_set.append(substring)

# 生成简化后的候选项集
substring_groups = group_substrings(result_set)
candidate_sum = candidate_sets(substring_groups)
print(f"Candidates:{candidate_sum}")

