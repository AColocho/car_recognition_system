import os
from tensorflow.keras.models import load_model
import tensorflow.keras.preprocessing.image as prep
import numpy as np
from PIL import Image
from flask import current_app

class ML:
    def PrepareData(self, image_path):
        '''
        Prepares image to be passed to a deep learning model. Transforms image to 100x100, grayscale, and normalizes array.
        Parameters:
            -image_path: path to the image.
        Returns:
            -Array for the image passed. 
        '''
        img_open = Image.open(image_path)
        image = img_open.resize((256,256))
        image = image.convert('RGB')
        
        array_image = prep.img_to_array(image)
        scaled_image = array_image * (1./255)
        image_to_array = np.array([scaled_image,scaled_image])
        
        return image_to_array
    
    def Predict(self, arrays):
        '''
        Uses saved model to predict image class. Model saved at flaskModel.h5
        Parameters:
            -Arrays: Array that contains two arrays of the same picture [array1, array1]
        Returns:
            -Probabily of image pertaining to a perticular class in the form of an array. 
        '''
        model = load_model('model.h5')
        return model.predict(arrays)[0]*100

class Logic:
        
    def RemoveImages(self):
        '''
        Removes any pictures in the temporary pictures folder.
        app/main/static/images
        '''
        
        dir_list = os.listdir(current_app.config['STATIC_IMAGES'])
        
        for data in dir_list:
            data_split = data.split('.')
            if 'txt' in data_split:
                pass
            else:
                os.remove(os.path.join(current_app.config['STATIC_IMAGES'],data))
    
    def CheckEmpty(self):
        '''
        Checks if the temporary picture folder is empty. 
        app/main/static/images
        '''
        
        dir_list = os.listdir(current_app.config['STATIC_IMAGES'])
        img = 0
        
        for data in dir_list:
            data_split = data.split('.')
            if 'txt' in data_split:
                pass
            else:
                img +=1
        
        if img == 0:
            return True
        else:
            return False
    
    def ReturnImagePath(self):
        '''
        Returns the image path to be used in the deep learning model.
        app/main/static/images
        '''
        dir_list = os.listdir(current_app.config['STATIC_IMAGES'])
        
        for data in dir_list:
            data_split = data.split('.')
            if 'txt' in data_split:
                pass
            else:
                return "{}/{}".format(current_app.config['STATIC_IMAGES'],data)
    
    def ReturnImagePath_css(self):
        '''
        Returns image path to display image.
        /static/images 
        '''
        dir_list = os.listdir(current_app.config['STATIC_IMAGES'])
        pic = []
        
        for data in dir_list:
            data_split = data.split('.')
            if 'txt' in data_split:
                pass
            else:
                pic.append(data)
                
        return "static/images/{}".format(pic[0])