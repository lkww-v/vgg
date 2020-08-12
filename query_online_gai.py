# -*- coding: utf-8 -*-
from extract_cnn_vgg16_keras import VGGNet
from photo_gai import Photo
import numpy as np
import os
import cv2
import h5py
import matplotlib.pyplot as plt   # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import argparse
'''
在线搜索部分query_online.py
相似度采用余弦相似度度量
'''

if __name__ == '__main__':
    Ph = Photo()
# read in indexed images' feature vectors and corresponding image names读取索引图像的特征向量和对应的图像名称
    h5f = h5py.File('add_after.h5', 'r')
    feats = h5f['dataset_1'][:]
    imgNames = h5f['dataset_2'][:]
    h5f.close()
    print("--------------------------------------------------")
    print("               searching starts")
    print("--------------------------------------------------")

    # read and show query image
    queryDir = "./datab/1.jpg"
    queryImg = mpimg.imread(queryDir)  # 读取和代码处于同一目录下的 queryDir
    #plt.title("Query Image")
    #plt.imshow(queryImg)  # 显示图片
    plt.show()

    # init VGGNet16 model
    model = VGGNet()

    # extract query image's feature, compute simlarity score and sort提取查询图像的特征，计算简单度和排序
    queryVec = model.extract_feat(queryDir)  # 修改此处改变提取特征的网络
    scores = np.dot(queryVec, feats.T)  # 矩阵乘法
    rank_ID = np.argsort(scores)[::-1]  # 将scores倒排
    rank_score = scores[rank_ID]
    # print rank_ID
    # print rank_score

    # number of top retrieved images to show
    maxres = 10
    imlist = []
    palist = []
    score = []
    for i, index in enumerate(rank_ID[0:maxres]):
        imlist.append(imgNames[index])
        #print(type(imgNames[index]))
        #print("image names: " + str(imgNames[index]) + " scores: %f" % rank_score[i])
        score.append(rank_score[i])
    #print("top %d images in order are: " % maxres, imlist)

    # show top #maxres retrieved result one by one
    for i, im in enumerate(imlist):

        if not os.path.exists('Download' + "/" + str(im, encoding='utf-8')):  # 如果路径不存在
            image = mpimg.imread('add_photo' + "/" + str(im, encoding='utf-8'))
            palist.append(str('add_photo' + "/" + str(im, encoding='utf-8')))
        else:
            image = mpimg.imread('Download' + "/" + str(im, encoding='utf-8'))
            #print("im is :" + 'Download' + "/" + str(im, encoding='utf-8'))
            palist.append(str('Download' + "/" + str(im, encoding='utf-8')))

    fl = open('./fs.txt', mode='w')
    file_handle = open('./list.txt', mode='w')
    #f = open('./score.txt', mode='w')
    for i in range(0,10):
        fl.write(palist[i]+": \t\t "+"%.4f" %score[i]+"\n")
        file_handle.write("./" + palist[i] + "\n")
        #f.write("%.4f" % score[i] + "\n")








