# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as LA
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

class VGGNet:
    def __init__(self):
        # weights: 'imagenet'
        # pooling: 'max' or 'avg'
        # input_shape: (width, height, 3), width and height should >= 48

        '''
        特征提取模块 extract_cnn_vgg16_keras.py
        # include_top：是否保留顶层的3个全连接网络
        # weights：None代表随机初始化，即不加载预训练权重。'imagenet'代表加载预训练权重,如果 weight = ‘imagenet’,
         则输入尺寸必须严格等于(224,224), 权重的规模和结构有出入唯一决定,
         使用了imagenet的权重,就必须使用训练时所对应的输入, 否则第一个全连接层的输入对接不上.
         (例如, 原来网络最后一个卷基层的输出为 300, 全连接层的神经元有1000个,则这里权重的结构为300X1000),
         而其他的出入不能保证卷基层输出为300, 则对接不上会报错). 
        # input_tensor：可填入Keras tensor作为模型的图像输出tensor
        # input_shape：可选，仅当include_top=False有效，应为长为3的tuple，指明输入图片的shape，
            图片的宽高必须大于48 (范围不得小于48, 否则最后一个卷积层没有输出)，如(200,200,3)
        #pooling：当include_top = False时(表示用网络进行特征提取), 此时需要指定输入图片尺寸。该参数指定了池化方式。
        如果include_top = True(表示网路被用来进行重新训练或fine-tune), 则图片输入尺寸必须在有效范围内(width & height 大于48)或和加载权重训练时的输入保持一致.
           None代表不池化，最后一个卷积层的输出为4D张量。‘avg’代表全局平均池化，‘max’代表全局最大值池化。
        #classes：可选，图片分类的类别数，仅当include_top = True并且不加载预训练权重时可用。
        如果include_top = False
        '''
        self.input_shape = (224, 224, 3)  #如果 weight = ‘imagenet’,则输入尺寸必须严格等于(224,224), 权重的规模和结构有出入唯一决定
        self.weight = 'imagenet'
        self.pooling = 'max'
        #调用已经训练好的vgg16
        self.model = VGG16(weights = self.weight,
                           input_shape = (self.input_shape[0], self.input_shape[1],self.input_shape[2]),
                                          pooling = self.pooling,include_top = False)
        self.model.predict(np.zeros((1, 224, 224 , 3)))
        #model.predict(test)预测的是数值,而且输出的还是5个编码值，不过是实数，预测后要经过argmax(predict_test,axis=1)
        #np.zeros返回来一个给定形状和类型的用0填充的数组，

    '''
    Use vgg16 model to extract features
    Output normalized feature vector
    '''
    '''
    #image.load_img()只是加载了一个文件，没有形成numpy数组，
#下面的numpy数组是通过image.img_to_array()的函数形成的
    '''
    def extract_feat(self, img_path):
        img = image.load_img(img_path, target_size=(self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img) # 三维（224，224，3）
        '''
        #读取完图像是三维向量，而模型输入要求四维
        # nums*weight*height*depth,输入模型前要扩展维度
         img = np.expand_dims(img, axis=0)
        '''
        img = np.expand_dims(img, axis=0)  # 四维（1，224，224，3）
        '''                              
        # 图像预处理
        #视自己情形是否需要图像预处理（如均值归一化处理等）
        img = preprocess_input(img)
        源码即在原有传入图片数组值(0-255)的基础之上，进行先除以 /127.5，然后减1，最后得到值得范围为(-1,1)
        预处理是从每个像素中减去在训练集上计算的RGB平均值。
        '''
        img = preprocess_input(img)     #预处理

        feat = self.model.predict(img)  #预测概率

        norm_feat = feat[0]/LA.norm(feat[0])
        return norm_feat