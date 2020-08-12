import cv2
import os
print("=============================================")
print("=  x: 拍摄图片                              =")
print("=  q: 退出                                  =")
print("=============================================")
print()
class_name = "E:\PycharmProjects\doutula\Image Searching Engine\datab2"
photo_name = input("请输入照片名：")
index = 1
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
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
        cv2.imwrite("%s/%s%d.jpg" % (class_name,photo_name, index),
                    cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA))
        print("%s: %d 张图片" % (class_name, index))
        index += 1
    if input == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
