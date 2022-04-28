from flask import Flask
import os
import const 
import json 
from tensorflow import keras
from flask import request, jsonify
import cv2
from flask import Response

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}




#curl --location --request POST 'http://127.0.0.1:5000/users' \
#--form 'image=@[YOUR_FILE_PATH]'

@app.route('/birdwatch', methods = ['POST']) 
def get_bird_predicitons():
    f  =request.files["image"]
    file_type=get_file_type(f.filename)
    if(allowed_file(f.filename, file_type)):
        f.save("./image."+file_type)
        model = keras.models.load_model('test_model')
        img = process_image(file_type)
        pred_array=make_predictions(model, img)
        predictions=build_dict(pred_array)
        res = json.dumps(predictions, indent = 4) 
        os.remove("image."+file_type)
        return Response({res}, status=200,mimetype='application/json')
    else:
        return Response({"Bad Request - invalid file"}, status=303)

def build_dict(pred_array):
    predictions={}
    for index, birdname in enumerate(const.COMMON_NAMES):
        predictions[birdname]=pred_array[index]
    return predictions

def make_predictions(model, img):
    preds = model.predict(img)[0]
    pred_array=str(preds)[1:-1].split()
    return pred_array
    
def process_image(file_type):
    theImage=cv2.imread("image."+file_type, cv2.IMREAD_COLOR)
    img_resize = cv2.resize(theImage, (256,256))
    img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
    img = img_rgb.reshape(1,256,256,3)
    return img
    
def get_file_type(filename):
    split_string = filename.rsplit('.', 1)
    print(len(split_string))
    file_ext = "invalid_file_extension" if len(split_string)<2 else  split_string[1].lower()
    return file_ext

def allowed_file(filename, file_type):
    return '.' in filename and file_type in ALLOWED_EXTENSIONS

@app.route('/')
def welcome():
    
    return Response({"Welcome to the Birdwatch Application"}, status=200,mimetype='text')

if __name__ == '__main__':
    app.run()


