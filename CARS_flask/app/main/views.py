from . import main
from flask import redirect, render_template, url_for,request, current_app
from app.main.functions import ML, Logic
import os
ML = ML()
L = Logic()

@main.route('/',methods=['GET', 'POST'])
def welcome():
    L.RemoveImages()

    if request.method == 'POST':
        if 'img' in request.files:
            file_upload = request.files['img']
            file_name = str(file_upload.filename).split('.')
            file_ext = file_name[-1]
            new_name = 'test_image.{}'.format(file_ext)
            file_upload.save(os.path.join(current_app.config['STATIC_IMAGES'],new_name))
            return redirect(url_for('main.results'))
        
    return render_template('index.html')

@main.route('/results',methods=['GET', 'POST'])
def results():
    
    if L.CheckEmpty():
        return redirect(url_for('main.welcome'))
    else:
        image = L.ReturnImagePath()
        image_arrays = ML.PrepareData(image)
        preds = ML.Predict(image_arrays)
        preds_perct = [str(round(x,2)) for x in preds]
        predictions = 'Known: {}% Unknown: {}%.'.format(preds_perct[0],preds_perct[1])
        css_img = L.ReturnImagePath_css()
        
            
        return render_template('results.html',preds=predictions,img=css_img)