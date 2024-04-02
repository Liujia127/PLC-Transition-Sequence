import pm4py
import csv
#
# # 读取pnml文件，生成事件日志
# net, im, fm = pm4py.read_pnml('handling_requests.pnml')
# log = pm4py.play_out(net, im, fm)
#
# # 把petri网模型生成的事件日志输出为xes文件
# pm4py.write_xes(log, "F:\\data\\h_r\\petri.xes")
#
#
# event_log = pm4py.read_xes("F:\\data\\h_r\\petri.xes")
# print(type(event_log))
# event_log.to_csv("F:\\data\\h_r\\petri.csv")

def import_xes(file_path):
    event_log = pm4py.read_xes(file_path)
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

    return event_log


if __name__ == "__main__":
    event_log = import_xes("F:\\data\\h_r\\0000.xes")
    df = pm4py.convert_to_dataframe(event_log)
    df.to_csv('F:\\data\\h_r\\petri.csv')