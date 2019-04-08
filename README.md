# YOLOv3-For-SVHN

credit from https://github.com/qqwweee/keras-yolo3

credit from https://github.com/penny4860/svhn-voc-annotation-format

# Work Before Training：
Besure the version of Keras and Tensorflow are same as mine

	conda create -n yolo python == 3.5	
	conda activate yolo
	pip install keras == 2.1.5
	pip install tensorflow == 1.6.0
	

Download images from http://ufldl.stanford.edu/housenumbers/

# Training
1. Download anntation of SVHN datast

		wget https://github.com/penny4860/svhn-voc-annotation-format/tree/master/annotation
2. Download Keras-YOLO3 model

		wget https://github.com/qqwweee/keras-yolo3

3. Download pretrain weight from [Here](https://drive.google.com/file/d/11ModH5nKTNh_zOLwqzTXTN1aGc7DM952/view?usp=sharing)  
It's original pretrain weight that converted into keras weight
