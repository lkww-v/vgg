import cv2
import os
import h5py
import numpy as np
from extract_cnn_vgg16_keras import VGGNet

class Photo:
    def get_imlist(path):
        return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
    class_name = "./datab"
    #photo_name = input("请输入照片名：")
    index = 1
    cap = cv2.VideoCapture(0)
    width = 640
    height = 480
    w = 360
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    crop_w_start = (width - w) // 2
    crop_h_start = (height - w) // 2

    while True:
        # get a frame
        ret, frame = cap.read()
        # show a frame
        frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]
        frame = cv2.flip(frame, 1, dst=None)
        cv2.imshow("capture", frame)

        input = cv2.waitKey(1) & 0xFF
        if input == ord('x'):
            cv2.imwrite("%s/%d.jpg" % (class_name, index),
                        cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA))
            #print("%s: %d 张图片" % (class_name, index))
            index += 1
        if input == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("--------------------------------------------------")
    print("                 拍照完成                   ")
    print("--------------------------------------------------")