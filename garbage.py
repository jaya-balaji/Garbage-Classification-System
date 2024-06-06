from __future__ import division, print_function
#coding=utf-8
import sys
import tensorflow as tf
import os
import glob

import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras import backend
from tensorflow.keras import backend
from tensorflow import keras
global graph
graph =tf.compat.v1.get_default_graph()

from skimage.transform import resize
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
#Define a flask app

#Load your trained model
model = load_model("templates\Garbage1.h5")
app = Flask(__name__, template_folder="templates" ,static_folder = "Static")



@app.route('/', methods=['GET'])

def index():
    return render_template("index.html")
@app.route('/Image', methods=['POST', 'GET'])
def prediction ():
    print("fnvn") # route which will take you to the prediction page
    return render_template("base.html")
    
@app.route('/predict', methods=['POST', 'GET'])
def upload():
    print("jvnb")
    print(request.method)
    if request.method == 'POST':
        print("hbhb")

        f = request.files['image']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'Predictions', f.filename)
        f.save(file_path)
        img = image.load_img(file_path, target_size=(128, 128))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        preds = model.predict(x)
        pred_class = np.argmax(preds)
        index = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
        text = "The Predicted Garbage is: " + index[pred_class]
        # ImageNet Decode
        print(text)
        return render_template("base.html", text=text)



app.run(debug=True)
