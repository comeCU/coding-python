#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_kmeans.py
# @Time    : 2019/3/26 12:05
# @Author  : dong

"""
用sklearn的k-means算法进行数据聚类

Reference：
    《python数据科学指南》
    blog：https://blog.csdn.net/jasonzhoujx/article/details/81942106
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans


def get_random_data():
    x_1 = np.random.normal(loc=0.2, scale=0.2, size=(10, 2))  # 10个2维的实例
    x_2 = np.random.normal(loc=0.9, scale=0.1, size=(10, 2))
    x = np.r_[x_1, x_2]  # 行堆叠函数，合并两个矩阵
    return x


def form_clusters(x, k):
    """创建簇

    :param x: 数据矩阵
    :param k: k是划分出的簇的个数
    :return:
    """
    no_clusters = k
    model = KMeans(n_clusters=no_clusters, init='random')
    model.fit(x)
    labels = model.labels_   # 获得结果标签，用来给每个点分配簇
    print(labels)
    # 计算轮廓系数
    sh_score = silhouette_score(x, labels)
    return sh_score


def draw_clusters(x_1, x_2, k):
    """绘制不同簇的点和聚类中心

    :param x_1: 样本数据矩阵
    :param x_2: 测试数据矩阵
    :param k: 轮廓系数最优对应的簇数
    :return:
    """
    no_clusters = k
    x = np.r_[x_1, x_2]  # 行堆叠函数，合并两个矩阵
    model = KMeans(n_clusters=no_clusters, init='random')
    model.fit(x)
    y_means = model.predict(x)  # 获取每个样本的簇标签
    print(y_means)

    # 可视化
    plt.scatter(x[:, 0], x[:, 1], c=y_means, cmap='viridis')
    centers = model.cluster_centers_
    print(centers)  # k-means算法确定的聚类中心
    plt.scatter(centers[:, 0], centers[:, 1], marker='+', c='r', s=200, alpha=0.5)

    # 设置图表标题并给坐标轴加上标签
    plt.title("draw_clusters figure", fontsize=24)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.show()


def get_sh_score_of_k(x, k):
    """获得不同k值的轮廓系数列表

    :param x: 数据矩阵
    :param k:  划分k-1个簇
    :return: 返回轮廓系数列表

    Notes
    -----
    轮廓系数用来评估k-means的结果，它的值介于 -1 ~ 1 之间，负值说明簇的半径大于簇之间的距离，
    也就是说两个簇之间有重叠，这说明聚类结果很差；而值越大，越接近1，则表明聚类结果越好。
    """
    sh_scores = []
    for i in range(1, k):
        sh_score = form_clusters(x, i+1)
        sh_scores.append(sh_score)
    return sh_scores


def draw_figure(k_low, k_hig, sh_scores):
    """绘制不同k值时生成的轮廓系数图形

    :param k_low:
    :param k_hig:
    :param sh_scores:
    :return:

    Notes
    -----
    [k_low, k_hig) 为左闭右开区间

    Examples
    -----
        draw_figure(2, 6, sh_scores)
        对应于k值为2,3,4,5 时的轮廓系数
    """
    no_clusters = []
    for i in range(k_low, k_hig):
        no_clusters.append(i)
    # no_clusters = [k_low for i in range(k_low, k_hig)]
    plt.figure(2)
    plt.plot(no_clusters, sh_scores)
    plt.title("Cluster Quality")
    plt.xlabel("No of clusters k")
    plt.ylabel("Silhouette Coefficient")
    plt.show()


if __name__ == '__main__':
    # print(get_random_data())

    # 绘制随机样本数据图
    x = get_random_data()
    plt.cla()
    plt.figure(1)
    plt.title("Generated data")
    plt.scatter(x[:, 0], x[:, 1])
    plt.show()

    # 绘制不同k值的轮廓系数图，以判断最合适数据集的k值
    my_sh_score = form_clusters(x, 2)
    print(my_sh_score)

    my_sh_scores = get_sh_score_of_k(x, 5)
    print(my_sh_scores)

    draw_figure(2, 6, my_sh_scores)

    # 测试画出不同的簇
    draw_clusters(x, np.zeros((0, 2)), 2)

