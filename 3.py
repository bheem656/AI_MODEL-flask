"""
Run a rest API exposing the yolov5s object detection model
"""
import argparse
import io
import json
import torch
from flask import Flask, request, render_template
from PIL import Image
from change_origin import convert
from werkzeug.utils import secure_filename
import os
import requests
# from io import BytesIO



app = Flask(__name__)

DETECTION_URL = "/v1/object-detection/yolov5s"
imaage_url = 'https://imgd.aeplcdn.com/0x0/n/cw/ec/56265/f-pace-exterior-right-front-three-quarter-2.jpeg'


# send = { }
# def result_append(res):
#     send = res.append(send)

# def final():
#         ret = eval(send)
#         ret = json.dumps(ret)
#         return ret

# result_1 = {}


def process(image_file):
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        height = img.height
        results = model(img)
        temp = results.pandas().xyxy[0].to_json(orient="records")
        res = convert(temp,height)
        # result_append(res)
        # result = eval(res)
        # result = json.dumps(res)

        return (res)

def process_url(im):
        img = Image.open(im)
        height = img.height
        print(height)
        results = model(img)
        temp = results.pandas().xyxy[0].to_json(orient="records")
        res = convert(temp,height)
        # result_append(res)
        # result = eval(res)
        # result = json.dumps(res)
        return (res)

rcvd = [
  {
    "images": [
      {
        "path": "https://m.media-amazon.com/images/I/41sGASjc4-L.jpg",
        "MediaFileId": 42479,
        "MemberIds": 236,
        "MissionId": 570,
        "Gufi": "8bf2d25b-fe18-4b09-b6bb-6735c5324aab"
      },
      {
        "path": "https://m.media-amazon.com/images/I/41sGASjc4-L.jpg",
        "MediaFileId": 42463,
        "MemberIds": 416,
        "MissionId": 570,
        "Gufi": "8bf2d25b-fe18-4b09-b6bb-6735c5324aab"
      }
    ],
    "issueToBeDetected": [
      {
        "Name": "Broken",
        "AnnotationTypeId": 211
      }
    ],
    "memberId": 236
  }
]

# garuda_url = '/garuda_poc'
mylist = []
mydata = []
mysend = None
def extract_path(x1):
    for x in range(len(x1)):
        for y in range(len(x1[x]['images'])):
            i1 = (x1[x]['images'][y]['path'])
            mylist.append(i1)
            # print(mylist)
    return mylist




@app.route('/detection', methods=["GET", "POST"])
def starting_url():
    # json_data = flask.request.json
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        mysend = json
        imag_data = extract_path(json)
        # print image url
        # for x in range(len(imag_data)):
        #     print(imag_data[x])
    else:
        return 'Content-Type not supported!'


    # response = requests.get(imag_data[0])
    # image_bytes = io.BytesIO(response.content)
    # converted_data = process_url(image_bytes)
    # print(converted_data)

    for x in range(len(imag_data)):
        response = requests.get(imag_data[x])
        image_bytes = io.BytesIO(response.content)
        converted_data = process_url(image_bytes)
        mysend[0]['images'][x]['data'] = converted_data
        print(converted_data)   
        # mydata.append[converted_data]

    #     # mylist.append(i1)

    # for p in range(len(imag_data)):
    #   for q in range(len(mysend[p]['images'])):
    #     response = requests.get(imag_data[p])
    #     image_bytes = io.BytesIO(response.content)
    #     converted_data = process_url(image_bytes)
    #     print(converted_data)   
        # mydata.append[converted_data]

        # mylist.append(i1)

    # mysend
    print(mysend)
    payload = {'Detected_payload': mysend}
    # print(b)
    return (payload)

# for p in range(len(x2)):
#     for q in range(len(x1[p]['images'])):
#         x2[p]['images'][q]['data'] = data


@app.route(DETECTION_URL)
def home():
    return render_template('detection.html')

@app.route(DETECTION_URL, methods=["POST"])
def predict():
    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        height = img.height
        results = model(img)
        temp = results.pandas().xyxy[0].to_json(orient="records")
        res = convert(temp,height)
        # result = eval(res)
        result = json.dumps(res)
        return (result)

# @app.route(DETECTION_URL)
# def home():
#     return render_template('detection.html')

# @app.route(DETECTION_URL, methods=["POST"])
# def predict():
#     if not request.method == "POST":
#         return "fail"

#     if request.files.get("image"):
#         image_file = request.files['file']
#         image_bytes = image_file.read()
#         img = Image.open(io.BytesIO(image_bytes))
#         height = img.height
#         results = model(img)
#         temp = results.pandas().xyxy[0].to_json(orient="records")
#         # print(temp)
#         res = convert(temp,height)
#         # result = eval(res)
#         result = json.dumps(res)
#         return "s"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load("ultralytics/yolov5", "yolov5s", force_reload=True)  # force_reload to recache
    app.run(host="0.0.0.0", port=args.port, debug=True)  # debug=True causes Restarting with stat
