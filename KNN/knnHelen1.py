#!/usr/bin/env python
# encoding: utf-8
"""
@author: scoefield
@file: knnHelen1.py
@time: 2018/2/10 22:51
"""
import numpy as np
from GraduationDesign.mysystempage import globalmodel
from tkinter import *
"""
函数说明:打开并解析文件，对数据进行分类：1代表不喜欢,2代表魅力一般,3代表极具魅力
Parameters:
    filename - 文件名
Returns:
    returnMat - 特征矩阵
    classLabelVector - 分类Label向量
"""
def file2matrix(filename):
    # 打开文件
    fr = open(filename)
    # 读取文件所有内容
    arrayOLines = fr.readlines()
    # 得到文件行数
    numberOfLines = len(arrayOLines)
    # 返回的NumPy矩阵,解析完成的数据:numberOfLines行,3列
    returnMat = np.zeros((numberOfLines, 3))
    # 返回的分类标签向量
    classLabelVector = []
    # 行的索引值
    index = 0
    for line in arrayOLines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        # 使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        listFromLine = line.split('\t')
        # 将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
        returnMat[index,:] = listFromLine[0:3]
        # 根据文本中标记的喜欢的程度进行分类,1代表不喜欢,2代表魅力一般,3代表极具魅力
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        index += 1
    return returnMat, classLabelVector


def knnshowdata1():
    # 打开的文件名
    filename = "mysystemdata/knnHelenData.txt"
    # 打开并处理数据
    datingDataMat, datingLabels = file2matrix(filename)

    globalmodel.get_value().delete(1.0, END)
    globalmodel.get_value().insert("insert", "--------------------------- 数据获取方式 ----------------------\n")
    globalmodel.get_value().insert("insert", "可以使用爬虫进行数据的收集，也可以使用第三方提供的免费或收费的数据。"
                                             "一般来讲，数据放在txt文本文件中，按照一定的格式进行存储，便于解析及处理。")
    globalmodel.get_value().insert("insert", "\n\n--------------------------- 解析数据集并显示 ---------------------\n")
    globalmodel.get_value().insert("insert", "收集的样本数据主要包含以下3种特征：\n"
                                             "1、每年获得的飞行常客里程数\n"
                                             "2、玩视频游戏所消耗时间百分比\n"
                                             "3、每周消费的冰淇淋公升数\n")
    globalmodel.get_value().insert("insert", "特征对应的数据：\n %s" % datingDataMat)
    globalmodel.get_value().insert("insert", "\n\n收集的样本数据分类标签：\n"
                                             "根据文本中标记的喜欢的程度进行分类,1代表不喜欢(didntLike),2代表魅力一般(smallDoses),3代表极具魅力(largeDoses)\n")
    globalmodel.get_value().insert("insert", "\n特征数据对应的分类标签：\n %s" % datingLabels)
    # print(datingDataMat)
    # print(datingLabels)


if __name__ == '__main__':
    knnshowdata1()
