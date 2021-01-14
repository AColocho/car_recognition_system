from tensorflow.keras.models import load_model
import tensorflow.keras.preprocessing.image as prep
import streamlit as st
from PIL import Image
import numpy as np
import io
import os

def main():
    #Functions to load model and predict the passed info
    def predict(arrays):
        '''
        Uses saved model to predict image class. Model saved at flaskModel.h5
        Parameters:
            -Arrays: Array that contains two arrays of the same picture [array1, array1]
        Returns:
            -Probabily of image pertaining to a perticular class in the form of an array. 
        '''
        model = load_model('model.h5')
        return model.predict(arrays)[0]*100
        
    def prepare_data(image_path):
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
    
    #Configuring page 
    st.set_page_config(page_title='CARS',page_icon=':racing_car:',initial_sidebar_state='collapsed')
    
    #Hiding hamburger menu
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>"""
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    main_container = st.beta_container()

    writing_container = main_container.beta_container()
    writing_container.title('CARS (Car Reconition System)')
    writing_container.write("I am an AI that is seeking to help with home security.")
    writing_container.write("I want to achieve this by learning what car(s) you drive and \
                            send you a notification when an unkown car pulls up to your drive way")
    writing_container.write("I do this by using the power of machine learning!")
    writing_container.markdown("You can find my source code [here](https://github.com/AColocho/car_recognition_system)")
    writing_container.write("So far, I was taught to recognize the Toyota Camry below.")

    picture_container = main_container.beta_container()
    picture_container.image(os.getcwd()+'/image/camry1.jpg')
    picture_container.image(os.getcwd()+'/image/camry5.jpg')

    interact_container = main_container.beta_container()
    interact_container.write("You can try to trick me by showing me a picture of your car! I've had promising success so far ;)")
    photo = interact_container.file_uploader('Upload photo',type=['png', 'jpg', 'jpeg'] )

    analysis = main_container.beta_container()
    if photo is not None:
        #Change image to bytesIO
        bytes_photo = io.BytesIO(photo.read())
        #Open Image
        PIL_photo = Image.open(bytes_photo)
        
        # Save image
        try:
            PIL_photo.save(os.getcwd()+'/image/test_image.jpeg')
        except: 
            PIL_photo.save(os.getcwd()+'/image/test_image.png')
        
        analysis.write('The photo you showed me.')
        
        # Show image
        try:
            analysis.image(os.getcwd()+'/image/test_image.jpeg')
        except:
            analysis.image(os.getcwd()+'/image/test_image.png')
        
        try:
            image_array = prepare_data(os.getcwd()+'/image/test_image.jpeg')
        except:
            image_array = prepare_data(os.getcwd()+'/image/test_image.png')
        
        predict = predict(image_array)
        preds_perct = [str(round(x,2)) for x in predict]
        
        prediction = "{}% Known  {}% Not Known".format(preds_perct[0],preds_perct[1])
        analysis.write(prediction)
        
if __name__ == "__main__":
    main()