import os
import h5py
import numpy as np
from extract_cnn_vgg16_keras import VGGNet
def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

h5f = h5py.File("featureCNN.h5",'r')
feats = h5f['dataset_1'][:]
imgNames = h5f['dataset_2'][:]
print("featureCNN.h5中特征值的个数：")
print(imgNames.shape)
#数组不支持append，那么解决办法就是等得到了完整的list再统一转为数组：

feats = feats.tolist()
imgNames = list(imgNames)
img_list = get_imlist("add_photo")  #获取db文件夹下的图片文件名(包括后缀名)
model = VGGNet()
#enumerate将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
for i, img_path in enumerate(img_list):
    norm_feat = model.extract_feat(img_path)#list
    Name = os.path.split(img_path)[1]  #os.path.split按照路径将文件名和路径分割开,[1]提取文件名
    feats.append(norm_feat)  #feats是list
    imgNames.append(Name.encode())
    print ("extracting feature from image No. %d , %d images in total" %((i+1), len(img_list)))
feats = np.array(feats)   #数组（矩阵）
f = h5py.File("add_after.h5", 'w')  # 创建一个h5文件，文件指针是h5f
f.create_dataset('dataset_1', data=feats)  # 根目录下创建一个dataset，一个组可由多个dataset组成，几个组构成一个h5文件
f.create_dataset('dataset_2', data=imgNames)
imgNames2 = f['dataset_2'][:]

print("add_after.h5中特征值的个数：")
print(imgNames2.shape)
f.close()
