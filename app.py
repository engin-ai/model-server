from flask import Flask, render_template, request
from PIL import Image
import requests


app = Flask(__name__)

ENV = 'dev'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods =['POST'])
def predict():
    if request.method=='POST':
        image_url = request.form.get('url')
        print(image_url)
        img = Image.open(requests.get(image_url, stream=True).raw)
    return {'imgsize':img.size}

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        return render_template('index.html', message='You have already submitted feedback')

if __name__ == '__main__':
    app.run()
