import xml.etree.ElementTree as ET
import os 

sets=['train',  'val',  'test']

classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def convert_annotation(image_set,image_id, list_file):
    an_dir='/home/ang/pywork/svhn/annotation/%s/%s.xml'%(image_set,image_id)
    in_file = open(an_dir)
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
       
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

for  image_set in sets:
    image_dir="/home/ang/pywork/svhn/image/%s"%image_set
    txt_dir='/home/ang/pywork/svhn/%s.txt'%image_set
    list_file=open(txt_dir,"w")

    for root, dirs, files in os.walk(image_dir) :
         file_min=min(files)
         png=file_min.find('.png')
         num_min=int(file_min[0:png])
         num=len(files)

    for image_id in range(num_min,num_min+num):
        list_file.write('/home/ang/pywork/svhn/image/%s/%s.png'%(image_set, image_id))
        convert_annotation(image_set,image_id, list_file)
        list_file.write('\n')
        
    list_file.close()
