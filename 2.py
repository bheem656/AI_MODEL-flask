import json
from PIL import Image
import requests
from io import BytesIO

from requests.models import Response



'''
[
  {
    "images": [
      {
        "path": "http://s3.ap-south-1.amazonaws.com/bluehawk-in/uploadinput/mission/8bf2d25b-fe18-4b09-b6bb-6735c5324aab/gallery/Broken1.jpg",
        "MediaFileId": 42479,
        "MemberIds": 236,
        "MissionId": 570,
        "Gufi": "8bf2d25b-fe18-4b09-b6bb-6735c5324aab"
      },
      {
        "path": "http://s3.ap-south-1.amazonaws.com/bluehawk-in/uploadinput/mission/8bf2d25b-fe18-4b09-b6bb-6735c5324aab/gallery/Broken2.jpg",
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
'''

# url = 'http://s3.ap-south-1.amazonaws.com/bluehawk-in/uploadinput/mission/8bf2d25b-fe18-4b09-b6bb-6735c5324aab/gallery/Broken1.jpg'

# JSON string
rcv = [
  {
    "images": [
      {
        "path": "http://s3.ap-south-1.amazonaws.com/bluehawk-in/uploadinput/mission/8bf2d25b-fe18-4b09-b6bb-6735c5324aab/gallery/Broken1.jpg",
        "MediaFileId": 42479,
        "MemberIds": 236,
        "MissionId": 570,
        "Gufi": "8bf2d25b-fe18-4b09-b6bb-6735c5324aab"
      },
      {
        "path": "http://s3.ap-south-1.amazonaws.com/bluehawk-in/uploadinput/mission/8bf2d25b-fe18-4b09-b6bb-6735c5324aab/gallery/Broken2.jpg",
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

data = [
  {
    "xmin": 51.7944984436,
    "ymin": 33.7292137146,
    "xmax": 322.1586914062,
    "ymax": 312.4273986816,
    "confidence": 0.8167709112,
    "class": 0,
    "name": "person"
  },
  {
    "xmin": 47.0410690308,
    "ymin": 135.5624084473,
    "xmax": 77.5586090088,
    "ymax": 164.5962219238,
    "confidence": 0.252784878,
    "class": 41,
    "name": "cup"
  }
]

send = rcv

# store the URL in url as 
# # parameter for urlopen
# url = "https://api.github.com"
  
# # store the response of URL
# response = urlopen(url)
  
# # storing the JSON response 
# # from url in data
# data_json = json.loads(response.read())


# Convert Python dict to JSON
rcv_json = json.dumps(rcv)
# print(rcv_json)

# Convert string to Python dict
x1 = json.loads(rcv_json)

# print (x1[0]['images'])



# getting all path from json
for x in range(len(x1)):
    for y in range(len(x1[x]['images'])):
        print (x1[x]['images'][y]['path'])


# changing response
send_json = json.dumps(send)
x2 = json.loads(send_json)

for p in range(len(x2)):
    for q in range(len(x1[p]['images'])):
        x2[p]['images'][q]['data'] = data

# print(json.dumps(x2,indent=4))


# response = requests.get(url)
# img = Image.open(BytesIO(response.content))

# print(img)