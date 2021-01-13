import streamlit as st
from PIL import Image
import io
import numpy as np
from CARS.logic import ML

main_container = st.beta_container()

writing_container = main_container.beta_container()
writing_container.title('CARS (CAr Reconition System')
writing_container.write("I am an AI that is seeking to help with home security.")
writing_container.write("I want to achieve this by learning what car(s) you drive and \
                        send you a notification when an unkown car pulls up to your drive way")
writing_container.write("I do this by using the power of machine learning!")
writing_container.write("So far, I was taught to recognize the Toyota Camry below.")

picture_container = main_container.beta_container()
picture_container.image('image/camry1.jpg')
picture_container.image('image/camry5.jpg')

interact_container = main_container.beta_container()
interact_container.write("You can try your own! Don't worry, the image will be deleted when the session is over.")
photo = interact_container.file_uploader('Upload photo')

analysis = main_container.beta_container()
if photo is not None:
    #Change image to bytesIO
    bytes_photo = io.BytesIO(photo.read())
    #Open Image
    PIL_photo = Image.open(bytes_photo)
    
    # Save image
    try:
        PIL_photo.save('image/test_image.jpeg')
    except: 
        PIL_photo.save('image/test_image.png')
    
    analysis.write('The photo you showed me.')
    
    # Show image
    try:
        analysis.image('image/test_image.jpeg')
    except:
        analysis.image('image/test_image.png')
    
    try:
        image_array = ML.prepare_data('image/test_image.jpeg')
    except:
        image_array = ML.prepare_data('image/test_image.png')
    
    predict = ML.predict(image_array)
    
    prediction = "{}% Known  {}% Not Known".format(predict[0],predict[1])
    analysis.write(prediction)