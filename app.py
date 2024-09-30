# Libraries

from flask import Flask, request
import requests
import json

from PIL import Image as PilImage
from io import BytesIO


# Functions

def clamp(Number, Min, Max):
    if Number < Min:
        return Min
    elif Number > Max: 
        return Max
    else: 
        return Number 


# App

app = Flask(__name__)

@app.route('/')
def Post():
    ImageURL = request.args.get("URL")
    ImageSizeX = int(request.args.get("SizeX"))
    ImageSizeY = int(request.args.get("SizeY"))
    ImageSize = [clamp(ImageSizeX, 10, 240), clamp(ImageSizeY, 10, 240)]
    
    Response = requests.get(ImageURL)
    NewImage = PilImage.open(BytesIO(Response.content)).resize(ImageSize)
    Data = list(NewImage.getdata())

    return json.dumps({
            "Data": Data,
            "Size": NewImage.size,
        })

app.run()
