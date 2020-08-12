# -*- coding: utf-8 -*-
import os
import h5py
import numpy as np
import argparse
from extract_cnn_vgg16_keras import VGGNet
'''
#存储索引模块：index.py
#argparse 模块可以让人轻松编写用户友好的命令行接口。
'''

ap = argparse.ArgumentParser()   #创建解析器
#包含要建立索引的图像的数据库的路径
ap.add_argument("-database", required = True,
    help = "Path to database which contains images to be indexed")   #添加参数，help为一个此选项作用的简单描述。

ap.add_argument("-index", required = True,
    help = "Name of index file")
args = vars(ap.parse_args())

'''
 Returns a list of filenames for all jpg images in a directory.
'''
def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
#os.path.join拼接目录
#os.listdir(）：返回输入路径下的文件和列表名称
'''
 Extract features and index the images
'''
if __name__ == "__main__":

    db = args["database"]
    img_list = get_imlist(db)  #获取db文件夹下的图片文件名(包括后缀名)

    print ("--------------------------------------------------")
    print ("         feature extraction starts")
    print ("--------------------------------------------------")
#代表list列表数据类型，列表是一种可变序列。
    feats = []
    names = []

    model = VGGNet()
    #enumerate将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feat(img_path)
        img_name = os.path.split(img_path)[1]  #os.path.split按照路径将文件名和路径分割开,[1]提取文件名
        feats.append(norm_feat)
        names.append(img_name.encode())
        print ("extracting feature from image No. %d , %d images in total" %((i+1), len(img_list)))

    feats = np.array(feats)   #数组（矩阵）
    # directory for storing extracted features 用于存储提取的特性的目录
    output = args["index"]   #命令行传入的参数

    print ("--------------------------------------------------")
    print ("      writing feature extraction results ...")
    print ("--------------------------------------------------")

    h5f = h5py.File(output, 'w')   #创建一个h5文件，文件指针是h5f
    h5f.create_dataset('dataset_1', data = feats)   #根目录下创建一个dataset，一个组可由多个dataset组成，几个组构成一个h5文件
    h5f.create_dataset('dataset_2', data = names)
    h5f.close()