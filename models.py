import cv2
import pandas as pd
from keras import backend
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications import resnet50, inception_v3, vgg16
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Input
from keras.optimizers import Adam
import numpy as np
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def get_model():
    base_model = ResNet50(weights='imagenet',include_top=False)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(7, activation='softmax')(x)
    print('create model ')
    model = Model(inputs=base_model.input, outputs=predictions)
    print('compiling')
    model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.0001),
              metrics=['acc'])
    print('model loading')
    model.load_weights(os.path.join(dir_path,'weights/best_050_epochs.h5'))
    model._make_predict_function()
    print('model loaded')
    return model 