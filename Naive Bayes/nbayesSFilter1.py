#!/usr/bin/env python
# encoding: utf-8
"""
@author: scoefield
@file: nbayesSFilter1.py
@time: 2018/2/7 11:46
"""

"""
函数说明:创建实验样本

Parameters:
    无
Returns:
    postingList - 实验样本切分的词条
    classVec - 类别标签向量
Author:
    Scoefield
"""
from GraduationDesign.mysystempage import globalmodel
from tkinter import *

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],           #切分的词条
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表侮辱类，0代表非侮辱类
    return postingList, classVec

def showData1():
    postingLIst, classVec = loadDataSet()
    globalmodel.get_value().delete(1.0, END)
    globalmodel.get_value().insert("insert", "切分的词条：\n")
    for each in postingLIst:
        globalmodel.get_value().insert("insert", each)
        globalmodel.get_value().insert("insert", "\n")
    globalmodel.get_value().insert("insert", "\n类别标签向量，1代表侮辱类，0代表非侮辱类:\n")
    globalmodel.get_value().insert("insert", classVec)


if __name__ == '__main__':
   showData()
