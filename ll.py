"""Perform test request"""
import pprint

import requests

DETECTION_URL = "http://192.168.0.101:5000/v1/object-detection/yolov5s"
TEST_IMAGE = "D:/AI_MODEL/project/oj_det_yolov5/yolov5/data/images/zidane.jpg"
image_data = open(TEST_IMAGE, "rb").read()
response = requests.post(DETECTION_URL, files={"image": image_data}).json()
pprint.pprint(response)