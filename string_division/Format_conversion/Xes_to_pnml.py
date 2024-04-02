import pm4py


if __name__ == "__main__":
    # 读取pnml文件，生成事件日志
    net, im, fm = pm4py.read_pnml('data/0005.pnml')
    # pm4py.view_petri_net(net, im, fm)
    log = pm4py.play_out(net, im, fm)

    # 把petri网模型生成的事件日志输出为xes文件
    pm4py.write_xes(log, "data/0005.xes")

    # 读取.xes文件
    log = pm4py.read_xes("data/0005.xes")
    net, im, fm = pm4py.discover_petri_net_alpha(log)
    pm4py.view_petri_net(net, im, fm)

    # 提取所有轨迹
    traces = [trace for trace in log]

    # 重放前 100 条轨迹
    for i in range(100):
        trace = traces[i]
        places = pm4py.algo.simulation.playout.apply(net, im, fm, trace)
        print(f"Replayed Trace {i + 1}: {places}")
