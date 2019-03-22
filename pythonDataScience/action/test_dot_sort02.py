#! usr/bin/python
# -*-coding:utf-8-*-

from numpy import *
import operator


# 准备数据集
def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# k-近邻算法
# in_x 所要测试的向量
# data_set 训练样本集，一行对应一个训练样本的所有特征，labels为目标变量
# k 所选的最近邻个数
def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]   # 得到data_set的行数
    # 求距离公式中的(A - B)
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set    # tile(A, (m, n)) 将数组A作为元素，构造m行 n列的新数组
    # (A - B)^2
    sq_diff_mat = diff_mat ** 2
    sq_distance = sq_diff_mat.sum(axis=1)   # (axis=1)为按行累加，返回一列。详细查看文档中的Example
    # 开平方，求得欧式距离
    distances = sq_distance ** 0.5
    # 每个点按距离从小到大依次排序
    sorted_dist_indicies = distances.argsort()  # 得到每个元素的排序序号

    class_count = {}    # 字典
    # 距离最近的前k 个点根据labels开始投票
    for i in range(k):
        vote_label = labels[sorted_dist_indicies[i]]    # sorted_dist_indicies[i] 排序后的第i个数在原来数组中的下标
        # 投票 + 1，否则 + 0
        class_count[vote_label] = class_count.get(vote_label, 0) + 1    # 从字典中获取key对应的value，没有key则返回0
    # 投票数从大到小排序
    # key=operator.itemgetter(1) 按照第二个元素即value的值逆序排序
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


# 测试
def classify_test(in_x):
    group, labels = create_data_set()
    # print group, labels
    return classify0(in_x, group, labels, 3)


print(classify_test([4, 0.3]))