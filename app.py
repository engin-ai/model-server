from flask import Flask, render_template, request
from PIL import Image
import requests
#from models import get_model
import numpy as np
#from tensorflow.keras.applications.resnet50 import preprocess_input

app = Flask(__name__)
model = None
ENV = 'dev'


@app.route('/')
def index():
    return render_template('index.html')

# def load_model():
#     global model 
#     model = get_model()
#     return model

def prepare_image(img):
    return np.array([img])


@app.route('/predict',methods =['POST'])
def predict():
    if request.method=='POST':
        image_url = request.form.get('url')
        print(image_url)
        img = np.array(Image.open(requests.get(image_url, stream=True).raw))
        #img= prepare_image(img)
        #pred = model.predict(img)[0]
        #indxs = np.argsort(pred)[-3:]
        #preds  = pred[indxs]
        #results ={}
        convert = {0:'None', 1:'PC', 2:'DC', 3:'FB',4:'FL', 5:'PCH',6:'DSU', 7:'BCH'}
        #for j,k in zip(indxs,preds):
            #results[convert[j]]=float(k)
        #import pdb;pdb.set_trace()
        results = {
                "name": "FPC",
                 "width":"3m",
                 "length":"2m",
                 "confidence":"0.94"
                }
    return {'imgsize':img.size,'damage':results,"detection_img_url":"https://res.cloudinary.com/dqwgbheqj/image/upload/v1588969686/00234_j8rc5k_dyi2pl.jpg"}

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        return render_template('index.html', message='You have already submitted feedback')

if __name__ == '__main__':
    #load_model()
    app.run()
