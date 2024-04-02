import frequent_items
# from all.data_processing import two
import matplotlib.pyplot as plt

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

# 分割不包含父串的候选项
def separate_candidate_set(parent, children):
    result = children[:]  # 创建一个新列表，初始值与children相同
    containing_parent = []
    remaining_strings = []
    i = 0
    while i < len(result) - 1:
        j = i + 1
        while j < len(result):
            if parent in result[i]:
                if result[i] in result[j]:
                    result[j] = result[j].replace(result[i], "")   #result按字符串长短排序
            j += 1
        if not result[i]:
            del result[i]
        else:
            i += 1
        # print(result)

    for str in result:
        if parent in str:
            containing_parent.append(str)
        elif str not in remaining_strings:
            remaining_strings.append(str)

    return containing_parent, remaining_strings

def generate_candidate_set(parent, children):
    for i in range(1, 2):
        candidate_set = []
        for string in children:
            max_repeat = find_repeatable_segment1(string, parent)
            if len(max_repeat) > 0:
                for repeat in max_repeat:
                    if repeat:
                        if repeat not in candidate_set:
                            candidate_set.append(repeat)
            else:
                candidate_set.append(string)
        i += 1
    # print(1)
    # print(candidate_set)
    remove_contained_substrings(candidate_set)
    # print(2)
    # print(candidate_set)

    for i in range(1, 5):
        new_candidate_set = []
        for substring in candidate_set:
            str1, str2 = find_repeatable_segment2(substring)
            if str1:
                if str1 not in new_candidate_set:
                    new_candidate_set.append(str1)
            if str2:
                if str2 not in new_candidate_set:
                    new_candidate_set.append(str2)
        candidate_set = new_candidate_set
        i += 1
    candidate_set = sorted(candidate_set, key=len)
    # print(2)
    # print(candidate_set)

    new_candidate_set=[]
    containing_parent, remaining_strings = separate_candidate_set(parent, candidate_set)
    for string in containing_parent:
        new_candidate_set.append(string)
    candidate_set=new_candidate_set

    return candidate_set

def find_repeatable_segment1(text, string):
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
        # print(repeatable_segment)

    return repeatable_segment


def find_repeatable_segment2(string):
    prefix = string[:1]
    for i in range(1, len(string)):
        first_substring = string[:i]
        second_substring = string[i:]
        suffix = first_substring[len(first_substring)-1:]
        if first_substring.startswith(second_substring):
            second_substring = ""
            return first_substring, second_substring
        if second_substring.startswith(prefix):
            if second_substring.endswith(suffix):
                return first_substring, second_substring
            else:
                second_substring = ""
                return first_substring, second_substring

    return string, ""


# 子字符串分组
substring_groups = group_substrings(frequent_items.substring_set)
# 生成简化后的候选项集
i = 1
cand = []
graph1 = []
for parent, children in substring_groups.items():
    # print(f"Parent: '{parent}', Children: {children}")
    candidate_sets = generate_candidate_set(parent, children)
    cand_fre = []
    num = 0
    for string in candidate_sets:
        count = frequent_items.data.count(string)
        # if count > two.sel_fre:
        if count > 0:
            num = count + num
            cand_fre.append((string, count))
    if cand_fre:
        graph1.append((parent, num))
        cand_fre.sort(key=lambda x: x[1], reverse=True)
        cand.append((parent, cand_fre))
        print(f"Candidate_set_{i}: {cand_fre}")
        i += 1

print(graph1)

