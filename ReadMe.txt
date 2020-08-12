开发环境：	
	#tensorflow-gpu 1.8 + keras
	#python 3.7 

1.先使用爬虫下载图像至Download，add_photo两个文件夹：
	Download文件夹：即海量的图像库，特征提取至featureCNN.h5中（python index.py -database Download -index featureCNN.h5）
	add_photo文件夹：存放后续需要更新的图像
	执行add_feature.py：作用是将原特征存储的文件featureCNN.h5与新照片的特征组合放入add_after.h5
2.	
	即时拍照的图像存储在datab文件夹中 ，特征提取至paozhao.h5中
	之前拍照存储的图像，放入datab2，特征提取至paozhao2.h5（此两个文件夹可以不管）


3.命令行示例：
	# 对Download文件夹内图片进行特征提取，建立索引文件featureCNN.h5
	python index.py -database Download -index featureCNN.h5

	# 使用Download文件夹内Download/labixiaoxin_40.jpg作为测试图片，在Download内以add_after.h5进行近似图片查找，并显示最近似的3张图片
	python query_online.py -query Download/labixiaoxin_40.jpg -index add_after.h5 -result Download
4.ui_down.py为爬虫界面(代码默认是下载至add_photo)
5.photo_ui.py为拍照比对界面（按键x为拍照，q为退出）







