#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2/9/2021 3:14 PM
# __software__ : PyCharm

'''

对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，
使得图中任意一对顶点u和v，若边(u,v)∈E(G)，则u在线性序列中出现在v之前。
通常，这样的线性序列称为满足拓扑次序(Topological Order)的序列，简称拓扑序列。
简单的说，由某个集合上的一个偏序得到该集合上的一个全序，这个操作称之为拓扑排序。

在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）：
每个顶点出现且只出现一次；
若A在序列中排在B的前面，则在图中不存在从B到A的路径。

'''

from collections import defaultdict