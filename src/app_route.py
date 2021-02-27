from flask import render_template, jsonify, Response, request
import os 
import json

def get_image_name(index, file_image_path):
    # index = int(request.args.get('index'))

    # file_image_path = "store_data/store_data_5.txt"
    total_file = int(((file_image_path.split("/")[-1]).split(".")[0]).split("_")[-1])

    with open(file_image_path) as f:
        content = f.readlines()

    list_image = [x.strip() for x in content] 
    image_path = list_image[index]

    result = {'code': 1000, \
            'data': {'image_path': image_path, 'index': index, 'total_file': total_file}}
    
    return result
