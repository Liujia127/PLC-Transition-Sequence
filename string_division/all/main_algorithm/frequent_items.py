from all.data_processing import two
from graphviz import Digraph

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
            if len(current_prefix) > 0 and current_node.freq >= 2:
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


def visualize_trie(root, max_depth=5):  # 设置最大深度
    dot = Digraph(comment='Trie')

    def add_nodes(node, prefix="", depth=0):
        if depth > max_depth:  # 控制深度
            dot.node(prefix, label=f"{prefix} ({node.freq})")
            return
        for char, child in node.children.items():
            new_prefix = prefix + char
            dot.node(new_prefix, label=f"{new_prefix} ({child.freq})")
            dot.edge(prefix, new_prefix)
            add_nodes(child, new_prefix, depth + 1)

# def visualize_trie(root):
#     dot = Digraph(comment='Trie')
#
#     def add_nodes(node, prefix=""):
#         for char, child in node.children.items():
#             new_prefix = prefix + char
#             dot.node(new_prefix, label=f"{new_prefix} ({child.freq})")
#             dot.edge(prefix, new_prefix)
#             add_nodes(child, new_prefix)
#
    # add_nodes(root)
    # dot.render('trie_structure', format='png', view=True)  # 生成并查看图像

# 黑盒识别
# data = "abcdabdcefgdabcdefgdabcdabcdefgdefgdabcdefgdefgdefgdefgdefgdabdcabcdabcdabdcabcda"
# data = "abcdeafghidjkleafgcmdnkoeafgcijdkleafghidjkleafghmndkoeafghmndkoeafgcmndkoeafghidjkleafghmndkoeafghmndkoeafgcmndkoeafghijdkleafgcmdnkoeafghijdkleafgcmndkoeafghijdkleafgcmdnkoeafghmndkoeafghmdnkoeafgcmndkoeafghijdkleafgcmndkoeafghijdkl"
# data = "abdehacdefbdegacdefdcefcdehabcegadbehacdegabcegabdehabdehabcegadbehadbehacdefbdegacdefbdegabdehacdefdcefcdehabdehabdehacdefbdegabcegabceg"
data = two.transition_seq
substring_freq = find_sorted_substrings(data)
substring_set = []
for substring, freq in substring_freq:
    print(f"Substring: '{substring}', Frequency: {freq}")
    substring_set.append(substring)
print(f"substring_freq ={substring_freq}")
print(f"substring_set ={substring_set}")

# # 在生成 Trie 树后调用可视化函数
# root = TrieNode()
# for i in range(len(data)):
#     insert_into_trie(root, data[i:])
# visualize_trie(root)