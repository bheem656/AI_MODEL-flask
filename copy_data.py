import os
import shutil



dst_path = "D:/AI_MODEL/Annotation_polygon/Annotation_tool/coco-annotator/car parts"
src_path = "D:/AI_MODEL/SITE/BOTICX/VISION/YOLO/OBJECT_DETECTION/DATA/TRAIN_DATA"

i = 1
while os.path.exists(dst_path + "/res%s" % i):
    i += 1
#print (i)
dst_name = dst_path + "/res%s" % i

def DIR_create() :
    oldmask = os.umask(000)
    os.makedirs(dst_name, 777)
    os.umask(oldmask)

def all_copy():
    shutil.copytree(src_path, dst_name)

#DIR_create()
all_copy()