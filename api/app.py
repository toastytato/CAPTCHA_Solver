import requests
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from flask import Flask
from itertools import product
from tensorflow.keras.models import load_model

""" FLASK APPLICATION """
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1> CAPTCHA_Solver</h1>"


@app.route("/process/<payload>", methods=['GET'])
def process(payload):
    res = requests.get("https://www.google.com/recaptcha/api2/payload?p=" +
                      payload, stream=True)
    response = {}
    if res.status_code == 200:
        
        ### load images from response ###
        bytes_im = BytesIO(res.content)
        cv_im = np.array(Image.open(bytes_im))
        image_array = interpret_collage(cv_im)
        
        ### load model ###
        model = load_model("test_model.h5")
        
        ### get and interpret predictions ###
        predictions = model.predict(image_array)
        
        ### craft response ###
        for i,prediction in enumerate(predictions):
            response[f"image_{i}"] = str(prediction)

        response["success"] = "successful image load..."
    else:
        response["error"] = "cannot find payload..."
    return response

@app.route("/test/bicycle", methods=['GET'])
def test():
    res = requests.get("https://lh3.googleusercontent.com/d/1AqD3M6-Rfwy4t52kiVhb5APgjgq23w56")
    response = {}
    if res.status_code == 200:
        
        ### load images from response ###
        bytes_im = BytesIO(res.content)
        cv_im = np.array(Image.open(bytes_im))
        image_array = interpret_collage(cv_im)
        
        ### load model ###
        model = load_model("test_model.h5")
        
        ### get and interpret predictions ###
        predictions = model.predict(image_array)
        
        ### craft response ###
        for i,prediction in enumerate(predictions):
            response[f"image_{i}"] = str(prediction)

        response["success"] = "successful image load..."
    else:
        response["error"] = "cannot find payload..."
    return response
    
def interpret_collage(image_collage : np.ndarray) -> list:
    dims = [(0,100), (100,200), (200,300)]
    return np.array([np.array(image_collage[d[0][0]:d[0][1],d[1][0]:d[1][1]]) for d in product(dims, dims)])
    
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    
    

    