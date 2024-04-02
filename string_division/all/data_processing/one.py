import xml.etree.ElementTree as ET

# 读取.xes文件
tree = ET.parse('../data/0006.xes')
root = tree.getroot()

# 添加命名空间前缀，用于XPath查询
namespace = {'xes': 'http://www.xes-standard.org/'}

# 用于跟踪已输出轨迹的字典
output_count = {}

# 用于存储连接的轨迹字符串
all_event_values = []



# 遍历每个轨迹(trace)
for trace in root.findall('.//xes:trace', namespace):
    # 初始化一个空字符串来保存事件的"value"
    event_values = []

    # 遍历轨迹中的每个事件
    for event in trace.findall('.//xes:event', namespace):
        # 获取事件的"value"属性值
        event_value = event.find('.//xes:string[@key="concept:name"]', namespace).get('value')
        event_values.append(event_value)

    # 将事件的"value"合并
    combined_event_value = ''.join(event_values)

    # 检查轨迹是否已经输出
    if combined_event_value not in output_count:
        # 更新轨迹的输出计数
        output_count[combined_event_value] = 1
    else:
        # 增加轨迹的输出计数
        output_count[combined_event_value] += 1

    # 连续输出轨迹
    for _ in range(output_count[combined_event_value]):
        all_event_values.append(combined_event_value)

# 输出每个轨迹的最终输出次数，按频率高低输出
sorted(output_count.items(), key=lambda x: x[1], reverse=True)
# for combined_event_value, count in output_count.items():
    # print(f"轨迹 '{combined_event_value}' 输出了 {count} 次")
