from tensorflow.keras.models import load_model
import tensorflow.keras.preprocessing.image as prep
import numpy as np
from PIL import Image

class ML:
    def predict(self, arrays):
        '''
        Uses saved model to predict image class. Model saved at flaskModel.h5
        Parameters:
            -Arrays: Array that contains two arrays of the same picture [array1, array1]
        Returns:
            -Probabily of image pertaining to a perticular class in the form of an array. 
        '''
        model = load_model('model.h5')
        return model.predict(arrays)[0]*100
    
    def prepare_data(self, image_path):
        '''
        Prepares image to be passed to a deep learning model. Transforms image to 100x100, grayscale, and normalizes array.
        Parameters:
            -image_path: path to the image.
        Returns:
            -Array for the image passed. 
        '''
        img_open = Image.open(image_path)
        image = img_open.resize((256,256))
        
        array_image = prep.img_to_array(image)
        scaled_image = array_image * (1./255)
        image_to_array = np.array([scaled_image,scaled_image])
        
        return image_to_array