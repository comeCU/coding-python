#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : dot_sort.py
# @Time    : 2019/3/24 11:44
# @Author  : dong

"""
对二维坐标轴上的点进行聚类.
    1. 对样本点数据可视化
    2. 根据可视化效果确定中心点（"人为"标记类别）
    3. 计算测试点到中心点的距离，根据最小距离原则确定类别
"""

import numpy as np
import csv
import matplotlib.pyplot as plt

import action.test_kmeans as km


def get_distance(v1, v2):
    """获取两向量欧式距离

    :param v1: 向量v1
    :param v2: 向量v2
    :return:
    """
    if len(v1) == len(v2):
        return np.linalg.norm(v1 - v2)
    else:
        print("输入错误")
    return None


def read_data(file_path):
    """读取数据文件，将数据存在列表中

    :param file_path: 数据文件路径
    :return: 文件数据列表，行数

    Notes
    -----
    读取文件中的数据保存在列表中，是字符格式，为方便后续可视化，
    需要将字符数据转为float型

    """
    csv_file = open(file_path)
    csv_reader_lines = csv.reader(csv_file)
    data = []
    lines = 0

    for read_line in csv_reader_lines:
        # print(read_line)
        for num in read_line:
            data.append(np.float64(num))    # string转为float
        lines += 1

    arr_data = np.array(data)   # 转为数组

    return arr_data, lines


def get_xarr_yarr(arr_data, i):
    """通过传入的数据列表，获得各维度（特征）的存储列表

    :param arr_data: 传入的数据列表
    :param i: 从该下标后一个元素开始获取值
    :return: x轴，y轴两个维度的存储列表
    """
    length = len(arr_data)
    # print(length)
    xarr = []
    yarr = []
    # i = 2   # 从第三个元素开始
    while i < length - 1:
        xarr.append(arr_data[i])
        yarr.append(arr_data[i+1])
        i += 2

    return xarr, yarr


def get_mark_xarr_yarr(arr_data, i):
    length = len(arr_data)
    xarr = []
    yarr = []
    markarr = []
    while i < length - 1:
        xarr.append(arr_data[i])
        yarr.append(arr_data[i + 1])
        markarr.append(arr_data[i + 2])
        i += 3

    return xarr, yarr, markarr


def get_matrix_t(data_file_path, start_flag):
    """合并两个维度的存储数组，保存在矩阵中，并将其转置

    :param data_file_path: 文件路径
    :param start_flag: 由get_xarr_yarr()引入，从该下标后一个元素开始获取值
    :return: 转置后的矩阵
    """
    arr_data, mat_lines = read_data(data_file_path)
    x1, y1 = get_xarr_yarr(arr_data, start_flag)
    # matrix1 = np.zeros((len(x1), len(y1)))
    matrix = np.vstack((x1, y1)).T    # 按列合并 再转置

    return matrix, mat_lines


def get_matrix_t_mark(list_data, i):
    x1, y1, m1 = get_mark_xarr_yarr(list_data, i)
    matrix = np.vstack((x1, y1, m1)).T

    return matrix


def draw_figure(matrix, matrix2, matrix3, title):
    """使用scatter()绘制散点图

    :param matrix: 转置后的矩阵
    :return:

    Notes
    -----
    scatter()
    x:横坐标 y:纵坐标 s:点的尺寸

    plot画点以后会用一条线串起来，而scatter只是单独的点而已
    """
    if any(matrix.tolist()):
        plt.scatter(matrix[:, 0], matrix[:, 1], c='b', marker='o', label='d', s=20)  # 对矩阵进行列切片操作
    if any(matrix2.tolist()):
        plt.scatter(matrix2[:, 0], matrix2[:, 1], c='r', marker='+', label='m', s=50)
    if any(matrix3.tolist()):
        plt.scatter(matrix3[:, 0], matrix3[:, 1], c='g', marker='o', label='t', s=20)
    plt.legend(loc='upper left')    # 标签在左上角

    # 设置图表标题并给坐标轴加上标签
    plt.title(title, fontsize=24)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)

    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()


def do_judge(mark_mat, test_mat, test_i):
    """读取测试集文件中的数据，判断其分类
    分类原则：根据该点到三个分类中心点的距离排序，欧式距离最小的点就是他的类别

    :param mark_mat: 人为标记点数据转化后的矩阵
    :param test_mat: 测试数据点转化后的矩阵
    :param test_i: test_data.csv中的第几项数据
    :return: 返回字典中最小值对应的键
    """
    xy_mat = mark_mat[:, :2]
    # length = len(xy_mat)    # 矩阵行数 即分类中心点的个数

    my_mark_list = mark_mat[:, 2].tolist()  # 矩阵转为列表
    # print(my_mark_list)

    dot_mat = test_mat[test_i:test_i+1]

    dict = {}
    for i in range(len(my_mark_list)):
        dict[my_mark_list[i]] = get_distance(np.mat(xy_mat[i]), dot_mat)

    return min(dict, key=dict.get)  # 返回字典中最小值对应的键


def do_judge_all(mark_mat, test_mat, mark_matrix_len):
    save_all_dict = {}
    for test_i in range(mark_matrix_len):
        save_all_dict[test_i] = mapping_classification_name(do_judge(mark_mat, test_mat, test_i))

    return save_all_dict


def mapping_classification_name(classes):
    if classes == 0:
        return "区域1"
    elif classes == 1:
        return "区域2"
    elif classes == 2:
        return "区域3"
    else:
        return "不存在该区域类别，无法判断"


if __name__ == '__main__':
    m1 = np.zeros((0, 0))
    m2 = np.zeros((0, 0))
    m3 = np.zeros((0, 0))

    print("###########  get_matrix_t()  将dot_data.csvz中的数据映射在矩阵中  ###############################")
    dot_matrix, dot_lines = get_matrix_t("dot_data.csv", 2)
    print(dot_matrix)
    print(dot_lines)

    draw_figure(dot_matrix, m2, m3, "dot_data figure")      # 1.画样本点

    print("###########  read_data()  读取mark_data.csv人为标记文件，将数据存在列表中  ########################")
    data, lines = read_data("mark_data.csv")
    print(data, lines)
    print(len(data))

    print("###########  get_mark_xarr_yarr()  将列表中的数据分割成三组  #####################################")
    x_arr, y_arr, mark_arr = get_mark_xarr_yarr(data, 0)
    print(x_arr, y_arr, mark_arr)

    print("###########  get_matrix_t_mark()  将mark_data.csv文件中的数据映射在矩阵中  #######################")
    mark_matrix = get_matrix_t_mark(data, 0)
    print(mark_matrix)

    draw_figure(m1, mark_matrix, m3, "mark_data figure")    # 2.画人工标记点

    print("###########  get_matrix_t()  将test_data.csv文件中的数据映射到矩阵中  ############################")
    test_matrix, test_lines = get_matrix_t("test_data.csv", 0)
    print(test_matrix)
    print(test_lines)

    draw_figure(dot_matrix, mark_matrix, test_matrix, "test_data figure")    # 3.画测试数据点

    print("###########  do_judge_all()  输出判断结果  ######################################################")
    # print(do_judge(mark_matrix, test_matrix, 3))
    print(do_judge_all(mark_matrix, test_matrix, len(test_matrix)), end='\n\n')

    print("================================================================================================")
    print("================================================================================================\n")
    print("###########  采用sklearn库的k-means进行数据聚类  #################################################")

    dot_sh_scores = km.get_sh_score_of_k(dot_matrix, 5)
    print("###########  簇系数  ###########################################################################")
    print(dot_sh_scores)
    km.draw_figure(2, 6, dot_sh_scores)

    print("###########  聚类标签 聚类中心  ##################################################################")
    km.draw_clusters(dot_matrix, test_matrix, dot_sh_scores.index(max(dot_sh_scores)) + 2)