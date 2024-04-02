import csv
import time


# 把划分好的变迁序列写入到csv文件中去
def generate_csv(partitions, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['case_id', 'activity','timestamp'])

        case_id = 1
        for partition in partitions:
            for transition in partition:
                # 获取当前时间戳
                timestamp = time.time()
                # 格式化时间
                time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
                writer.writerow([case_id, transition,time_str])
                case_id += 1


data = [list('efgd'), list('abcd'), list('abcdabdc'), list('efgdabdc')]
filename = "one.csv"
data1 = [list('mndkoeafgh'), list('mndkoeafgc'), list('mdnkoeafgc'), list('mdnkoeafgh'), list('ijdkl'), list('idjkl'), list('eafgc'), list('eafgh')]
filename = "two.csv"
# mndkoeafgh 9，mndkoeafgc 4，mdnkoeafgc 3，mdnkoeafgh 1，ijdkl 9，idjkl 3，eafgc 5，eafgh 7
generate_csv(data, filename)