����������	
	#tensorflow-gpu 1.8 + keras
	#python 3.7 

1.��ʹ����������ͼ����Download��add_photo�����ļ��У�
	Download�ļ��У���������ͼ��⣬������ȡ��featureCNN.h5�У�python index.py -database Download -index featureCNN.h5��
	add_photo�ļ��У���ź�����Ҫ���µ�ͼ��
	ִ��add_feature.py�������ǽ�ԭ�����洢���ļ�featureCNN.h5������Ƭ��������Ϸ���add_after.h5
2.	
	��ʱ���յ�ͼ��洢��datab�ļ����� ��������ȡ��paozhao.h5��
	֮ǰ���մ洢��ͼ�񣬷���datab2��������ȡ��paozhao2.h5���������ļ��п��Բ��ܣ�


3.������ʾ����
	# ��Download�ļ�����ͼƬ����������ȡ�����������ļ�featureCNN.h5
	python index.py -database Download -index featureCNN.h5

	# ʹ��Download�ļ�����Download/labixiaoxin_40.jpg��Ϊ����ͼƬ����Download����add_after.h5���н���ͼƬ���ң�����ʾ����Ƶ�3��ͼƬ
	python query_online.py -query Download/labixiaoxin_40.jpg -index add_after.h5 -result Download
4.ui_down.pyΪ�������(����Ĭ����������add_photo)
5.photo_ui.pyΪ���ձȶԽ��棨����xΪ���գ�qΪ�˳���







