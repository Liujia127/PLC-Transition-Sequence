import pm4py
from pm4py.objects.log import obj as log_instance

# 定义数据
data = ['mndkoeafgh', 'mndkoeafgc', 'mdnkoeafgc', 'mdnkoeafgh', 'ijdkl', 'idjkl', 'eafgc', 'eafgh']
# 频率大于2产生的数据
data1 = ['aclbph', 'aclbpj', 'aclbiobph', 'acdkclbph', 'aclbgobpj', 'aclbiobpj', 'acdkclbiobph', 'acmfenkclbph',
         'acmefnkclbpj', 'acdkcdkclbpj', 'acmfenkclbpj', 'aclbgobgobpj', 'acmefnkclbph', 'aclbgobph',
         'acdkclbiobpj', 'aclbiobiobpj', 'aclbiobgobph', 'aclbgobgobph', 'acdkcdkclbph', 'aclbiobiobph',
         'acdkclbiobiobph', 'acdkclbgobph', 'acmfenkclbiobpj', 'acmefnkclbiobgobpj', 'aclbiobiobiobpj',
         'aclbgobiobpj', 'aclbgobiobph', 'acdkcmefnkclbph','acdkclbpj', 'aclbiobgobiobpj', 'aclbgobgobiobpj',
         'aclbgobgobiobph', 'acdkclbgobpj', 'acdkcdkclbgobpj', 'acdkcdkclbgobph', 'acdkcdkclbgobiobph',
         'acdkcdkcdkclbpj', 'acdkcdkcdkclbph', 'acmfenkcmfenkclbpj', 'acmfenkclbiobph', 'acmfenkclbiobiobgobgobph',
         'acmfenkclbiobgobpj', 'acmfenkclbgobph', 'acmfenkclbgobgobpj', 'acmfenkcdkclbpj', 'acmfenkcdkclbgobph',
         'acmefnkcmfenkclbph', 'acmefnkclbgobpj', 'acmefnkcdkclbph', 'aclbgobiobiobpj', 'aclbgobiobgobpj',
         'acdkcmfenkcmfenkcdkclbpj', 'acdkcmfenkclbpj', 'acdkcmfenkcdkclbph', 'acdkcmefnkclbpj', 'acdkclbgobgobpj']
# 频率大于1%即5产生的数据
data2 = ['aclbph','aclbpj','aclbiobph','acdkclbph','aclbgobpj','aclbiobpj','acdkclbiobph','acmfenkclbph','acmefnkclbpj',
         'acdkcdkclbpj','acmfenkclbpj','aclbgobgobpj','acmefnkclbph','aclbgobph','acdkclbiobpj','aclbiobiobpj',
         'aclbiobgobph','aclbgobgobph','acdkcdkclbph','aclbiobiobph','acdkclbiobiobph','acdkclbgobph']
# 频率大于1%即10产生的数据
data3 = ['aclbph','aclbpj','aclbiobph','acdkclbph','aclbgobpj','aclbiobpj','acdkclbiobph','acmfenkclbph','acmefnkclbpj']

data4 = ['abcd', 'efgdabcd', 'abdc', 'efgd']
data5 = ['abdeh', 'adceg', 'acdefbdeg', 'adbeh', 'acdefdcefcdeh', 'acdeg']
data6= ['jacghl', 'jcaghl', 'jcghal', 'jcgahl', 'mbdfk', 'mdfbk', 'mbdindfk', 'mbdendfk', 'mdbfk', 'mdebndfk', 'mbdindindfk']
data7=['jacghl', 'jcaghl', 'jcghal', 'jcgahl', 'mbdfk', 'mdfbk', 'mbdindfk', 'mbdendfk', 'mdbfk', 'mdebndfk', 'mbdindindfk', 'mdibndfk', 'mdbendfk', 'mbdendindfk', 'mbdindendfk', 'mdbindfk', 'mbdendendfk', 'mdibndindfk', 'mdenbdfk', 'mdindfbk', 'mbdindindindfk', 'mdbindendfk', 'mdinbdfk']
data8 = ['jibgh','jigbh','jgibh','jbigh','jkbgh','jgbkefh', 'jgbkafh', 'jkbeh','jbkagfh','jgkabfh', 'jgkbfh', 'jkgbeh', 'jbgkcfh', 'jkebgfh', 'jkfgh', 'jkcah', 'jgkbah', 'jgkcah', 'jkgafh', 'jgbkfah', 'jbkgefh', 'jbkegh','jkcebh','jgkafbh','jbgkefh','jbgkafh','jbgkfeh','jbgkfah','jbkfgdh','jkabgfh','jgkecfdh','jgkfah', 'jbkceh', 'jbkfeh', 'jkefgh', 'jkecbh', 'jkgbfh', 'jgkbefh', 'jgkefdh', 'jgbkcfh', 'jkagfdh', 'jkbafgh', 'jkebfgh', 'jgkfch',  'jgkfdh',  'jbkech',  'jbkcah',  'jbkgch',  'jkafbh',  'jkbfeh',  'jkbceh',  'jkegch',  'jkfbgh',  'jkgefh',  'jkgfah',  'jkgcfh',  'jkcfbh',  'jkcbgh',  'jgkfedh',  'jgkafdh',  'jgbkfdh',  'jbkefgh',  'jkabfdh',  'jkafgbh',  'jkfebdh',  'jgkfbh', 'jgkach', 'jbkcfh', 'jbkgah', 'jkbcah', 'jkfegh', 'jkfcdh', 'jkfcbh', 'jkfcah', 'jkgcah', 'jkgbah', 'jkcgeh', 'jgkcfbh', 'jbgkfdh', 'jbkefdh', 'jbkgfdh', 'jbkfgch', 'jbkfcdh', 'jkabfch', 'jkbafdh', 'jkfabch', 'jkcbfgh', 'jkcgbfh', 'jgbkfcdh', 'jkagbfdlh', 'jbgih', 'jkegbfdlh', 'jgkabcfdlh', 'jkbcfdeglh', 'jkacgfbdlh', 'jgbih', 'jgkecbfdlh', 'jkfabgdlh', 'jkfbagdlh', 'jkfbcdalgh', 'jkegfbdlh', 'jkafdblgh', 'jkebfdglh', 'jkfagcdlbh', 'jgbkfedlh', 'jgbkfcadlh', 'jkabgcfdlh', 'jkfagcdblh', 'jgbkcafdlh', 'jgkcfebdlh', 'jgkefbdlh', 'jkfecdlgbh', 'jbkgfadlh', 'jkfdgbalh', 'jkefdglbh', 'jkbcgefdlh', 'jbgkecfdlh', 'jgkfebdlh', 'jgkcfdbalh', 'jkebcgfdlh', 'jkagfcbdlh', 'jkcbegfdlh', 'jkfagbdlh', 'jkgfdeblh', 'jkgebfdlh', 'jgbkecfdlh','jgkbcafdlh', 'jbkfcegdlh', 'jbgkcafdlh', 'jbkagcfdlh',  'jkcgabfdlh','jkcgbafdhl', 'jkfbegdhl', 'jkecgbfdhl', 'jkgabfdlh',  'jkefbdglh', 'jkabfgdlh', 'jkgfbdalh', 'jkafcgdlbh', 'jgkebfdlh',  'jbkfgadlh', 'jkagfbdlh',  'jbkacgfdlh', 'jkfacbgdlh', 'jbkfcadglh', 'jbkfgecdlh', 'jgbkcefdlh', 'jkcfadgblh', 'jkcgbefdlh', 'jkgfcebdlh', 'jkcgfbedlh', 'jkfebcgdlh', 'jkbacgfdlh', 'jbgkcefdlh', 'jbkgecfdlh', 'jgkcebfdlh', 'jkbfcagdlh', 'jkfcebdlgh', 'jkacgbfdlh', 'jgkefcdlbh', 'jkefcgdlbh', 'jgkafcbdlh', 'jkgbcfadlh', 'jkfbacdlgh', 'jbkafgdlh', 'jbkgfcdelh', 'jkbagfdlh', 'jkecfdgblh', 'jkcefgdlbh', 'jkfedglbh', 'jkafcbdglh', 'jbkgfedhl', 'jkebfdlgh', 'jkfadlbgh', 'jkcegbfdlh', 'jbkcgafdlh', 'jkbafcgdlh', 'jkbfgadlh', 'jgbkacfdlh', 'jbkfagdlh', 'jgkfecbdlh', 'jkgfbcdalh', 'jkgfcdablh', 'jkbfagdlh', 'jbkfdeglh', 'jgkfecdblh', 'jkgacbfdlh', 'jkcgfdelbh', 'jbkfcgadlh', 'jkegfcbdlh','jgkcfdablh','jkcgfedlbh']
data9=['ae', 'aie', 'bhfcgd', 'bhcfgd', 'bhcgfd','bhfc', 'bhcf', 'bhcf']
Log = log_instance.EventLog()
for string in data9:
    # 定义一个空的trace
    trace = log_instance.Trace()
    for i in range(len(string)):
        # 定义一个新的事件
        event = log_instance.Event()
        event['concept:name'] = string[i]
        trace.append(event)
    Log.append(trace)

# 使用Alpha算法生成Petri网
# net, im, fm = pm4py.discover_petri_net_alpha(Log)
net, im, fm = pm4py.algo.discovery.alpha.algorithm.apply(Log)
pm4py.view_petri_net(net, im, fm)
# pm4py.write_xes(Log, "log_xes")

