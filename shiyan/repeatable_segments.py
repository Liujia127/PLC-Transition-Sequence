import two
import matplotlib.pyplot as plt

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

def find_sorted_substrings(string):
    root = TrieNode()
    n = len(string)

    # 从后缀数组中逆序遍历后缀并插入到 Trie 树中
    for i in range(n - 1, -1, -1):
        suffix = string[i:]
        if len(suffix) > 1:  # 仅考虑长度大于1的后缀
            insert_into_trie(root, suffix)

    # 使用迭代方式遍历 Trie 树以获取所有出现频率大于等于2的子串
    def find_substring_frequent(node, prefix):
        result = []
        stack = [(node, prefix)]
        while stack:
            current_node, current_prefix = stack.pop()
            if len(current_prefix) > 1 and current_node.freq >= 4:
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


# 删除被其他子串包含的子串
def remove_contained_substrings(children):
    i = 0
    while i < len(children) - 1:
        j = i + 1
        while j < len(children):
            if children[i] in children[j]:
                children.pop(i)
                i = 0  # 重新从第一个字符串开始检查
                break
            elif children[j] in children[i]:
                children.pop(j)
                i = 0  # 重新从第一个字符串开始检查
                break
            j += 1
        else:
            i += 1


def generate_candidate_sets(parent, children):
    remove_contained_substrings(children)

    new_candidate_sets = []
    for substring in children:
        str1, str2 = find_repeatable_segment1(substring)
        if str1:
            if str1 not in new_candidate_sets:
                new_candidate_sets.append(str1)
        if str2:
            if str2 not in new_candidate_sets:
                new_candidate_sets.append(str2)
    candidate_sets = new_candidate_sets

    for string in children:
        max_repeat = find_repeatable_segment2(string, parent)
        if len(max_repeat) > 0:
            for repeat in max_repeat:
                if repeat:
                    if repeat not in candidate_sets:
                        candidate_sets.append(repeat)
        else:
            candidate_sets.append(string)

    new_candidate_sets = []
    for substring in candidate_sets:
        str1,str2 = find_repeatable_segment1(substring)
        if str1:
            if str1 not in new_candidate_sets:
                new_candidate_sets.append(str1)
        if str2:
            if str2 not in new_candidate_sets:
                new_candidate_sets.append(str2)
    candidate_sets = new_candidate_sets

    remove_contained_substrings(candidate_sets)
    return candidate_sets


def find_repeatable_segment1(string):
    prefix = string[:1]
    for i in range(1, len(string)):
        first_substring = string[:i]
        second_substring = string[i:]

        if first_substring.startswith(second_substring):
            second_substring = ""
            return first_substring, second_substring
        if second_substring.startswith(prefix):
            return first_substring, second_substring
    return string, ""


def find_repeatable_segment2(text, string):
    n = len(text)
    max_length = 0
    repeatable_segment = []

    for window_size in range(2, n // 2 + 1):
        for start in range(n - window_size + 1):
            segment = text[start:start + window_size]
            repeats = []

            for i in range(start + window_size, n - window_size + 1):
                if segment == text[i:i + window_size]:
                    repeats.append(segment)

            if len(repeats) > 0:
                if window_size > max_length and segment.startswith(string):
                    max_length = window_size
                    repeatable_segment = [segment]
                elif window_size == max_length and segment.startswith(string):
                    repeatable_segment.append(segment)

    return repeatable_segment


data = two.result_string3
substring_freq = find_sorted_substrings(data)
substring_set = []
for substring, freq in substring_freq:
    print(f"Substring: '{substring}', Frequency: {freq}")
    substring_set.append(substring)

# 子字符串分组
substring_groups = group_substrings(substring_set)

# 生成简化后的候选项集
i = 1
graph1 = []
for parent, children in substring_groups.items():
    # print(f"Parent: '{parent}', Children: {children}")
    candidate_sets = generate_candidate_sets(parent, children)
    cand_fre = []
    num = 0
    for string in candidate_sets:
        count = data.count(string)
        num = count + num
        cand_fre.append((string, count))
    graph1.append((parent, num))
    if len(candidate_sets) > 1:
        print(f"Candidate_sets_{i}: {candidate_sets}")
        print(cand_fre)
        print(num)
        i += 1

# 绘图
labels, values = zip(*graph1)
font = {'family': 'SimHei'}
plt.rc('font', **font)
plt.figure(figsize=(6, 6))  # 设置图形大小
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)  # 创建饼状图
plt.title('数据分布')  # 设置标题
plt.axis('equal')  # 使饼状图保持圆形
plt.show()  # 显示图形

