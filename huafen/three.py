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

# 示例用法
children = ["abc", "ab", "abcd", "xyz", "abc"]
remove_contained_substrings(children)
print(children)
