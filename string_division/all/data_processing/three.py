input_string = '''t1 t2 t3 t4 t5 t1 t6 t7 t8 t9 t4 t10 t11 t12 t5 t1 t6 t7 t3 t13 t4 t14 t11 t15 t5 t1 t6 t7 t3 t9 t10 
t4 t11 t12 t5 t1 t6 t7 t8 t9 t4 t10 t11 t12 t5 t1 t6 t7 t8 t13 t14 t4 t11 t15 t5 t1 t6 t7 t8 t13 t14 t4 t11 t15 t5 t1 
t6 t7 t3 t13 t14 t4 t11 t15 t5 t1 t6 t7 t8 t9 t4 t10 t11 t12 t5 t1 t6 t7 t8 t13 t14 t4 t11 t15 t5 t1 t6 t7 t8 t13 t14 
t4 t11 t15 t5 t1 t6 t7 t3 t13 t14 t4 t11 t15 t5 t1 t6 t7 t8 t9 t10 t4 t11 t12 t5 t1 t6 t7 t3 t13 t4 t14 t11 t15 t5 t1 
t6 t7 t8 t9 t10 t4 t11 t12 t5 t1 t6 t7 t3 t13 t14 t4 t11 t15 t5 t1 t6 t7 t8 t9 t10 t4 t11 t12 t5 t1 t6 t7 t3 t13 t4 t14 
t11 t15 t5 t1 t6 t7 t8 t13 t14 t4 t11 t15 t5 t1 t6 t7 t8 t13 t4 t14 t11 t15 t5 t1 t6 t7 t3 t13 t14 t4 t11 t15 t5 t1 t6 
t7 t8 t9 t10 t4 t11 t12 t5 t1 t6 t7 t3 t13 t14 t4 t11 t15 t5 t1 t6 t7 t8 t9 t10 t4 t11 t12'''
input_string1 = '''t1 t2 t3 t4 t1 t2 t4 t3 t5 t6 t7 t4 t1 t2 t3 t4 t5 t6 t7 t4 t1 t2 t3 t4 t1 t2 t3 t4 t5 t6 t7 t4 t5 t6 t7 t4 t1 t2
t3 t4 t5 t6 t7 t4 t5 t6 t7 t4 t5 t6 t7 t4 t5 t6 t7 t4 t5 t6 t7 t4 t1 t2 t4 t3 t1 t2 t3 t4 t1 t2 t3 t4 t1 t2 t4 t3 t1 t2 t3
t4 t1'''
# 去掉字符串中的空格
input_string = input_string.replace(' ', '')

# 将数字替换为字母
for i in range(10, 16):
    input_string = input_string.replace(f"t{i}", chr(ord('a') + i - 1))
for i in range(1, 10):
    input_string = input_string.replace(f"t{i}", chr(ord('a') + i - 1))

print(input_string, end='')
