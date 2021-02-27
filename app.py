from flask import Flask, render_template, jsonify, Response, request
import cv2
import os
import sys
import time
import logging
import traceback
import numpy as np 

from utils.parser import get_config
from utils.utils import create_folder

from src.app_route import get_image_name

# setup config
cfg = get_config()
cfg.merge_from_file('configs/service.yaml')
cfg.merge_from_file('configs/rcode.yaml')

HOST = cfg.SERVICE.SERVICE_IP
PORT = cfg.SERVICE.SERVICE_PORT
RCODE = cfg.RCODE

STORE_PATH = cfg.SERVICE.STORE_PATH
LOG_PATH = cfg.SERVICE.LOG_PATH
LABEL_PATH = cfg.SERVICE.LABEL_PATH

# create folder
create_folder(STORE_PATH)
create_folder(LOG_PATH)
create_folder(LABEL_PATH)

# create logging
logging.basicConfig(filename=os.path.join(LOG_PATH, str(time.time())+".log"), filemode="w", level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
logging.getLogger("").addHandler(console)
logger = logging.getLogger(__name__)
####################################

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def view_home():
    return render_template('index.html')

@app.route('/get_img_name')
def get_info_image():
    index = int(request.args.get('index'))
    file_image_path = "store_data/store_data_5.txt"

    result = get_image_name(index, file_image_path)
    print(result)

    return jsonify(result)

@app.route('/get_img')
def drawImagePath():
    print("showed image")
    filepath = request.args.get('filepath')
    print("filepath: ", filepath)

    img = cv2.imread(filepath)
    ret, jpeg = cv2.imencode('.jpg', img)

    return  Response((b'--frame\r\n'
                     b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tostring() + b'\r\n\r\n'),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)