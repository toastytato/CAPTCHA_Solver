import requests
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "<h1> CAPTCHA_Solver</h1>"


@app.route("/process/<payload>", methods=['GET'])
def process(payload):
    res = requests.get("https://www.google.com/recaptcha/api2/payload?p=" +
                      payload, stream=True)
    if res.status_code == 200:
        bytes_im = BytesIO(res.content)
        cv_im = cv2.cvtColor(np.array(Image.open(bytes_im)), cv2.COLOR_RGB2BGR)
        print(cv_im)
        return({"data":str(cv_im)})
    else:
        print("ruh-oh")
        return("ruh-oh")