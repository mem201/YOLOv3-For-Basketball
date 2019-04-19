import xml.etree.ElementTree as ET
import os 

sets=['train', 'test']

classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def convert_annotation(image_set,image_id, list_file):
    #where the annotation of the dataset at
    an_dir ='/home/ang/pywork/svhn/annotation/%s/%s.xml'%(image_set,image_id)
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
    #your dataset direction
    image_dir="/home/ang/pywork/svhn/image/%s/"%image_set
    
    #where you save the text file
    txt_dir='/home/ang/pywork/svhn/%s.txt'%image_set
    
    list_file=open(txt_dir,"w")
    file_name=[]
    for root, dirs, files in os.walk(image_dir) :
        for a in files:
          file_name.append(a)

    for image_id in file_name:
        num_png=image_id.find('.png')
        file=str(image_id[0:num_png])
        list_file.write(str(image_dir+image_id))
        convert_annotation(image_set, file, list_file)
        list_file.write('\n')
        
    list_file.close()
