import os 

def create_folder(path_folder):
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)

def write_image_path(path_folder):
    file_list = os.listdir(path_folder)
    total_file = len(file_list)
    text_name = path_folder.split("/")[-1] + '_{}.txt'.format(total_file)
    text_path = os.path.join(path_folder, text_name)
    
    with open(text_path, "a+") as f:
        for file_name in file_list:
            image_path = os.path.join(path_folder, file_name)
            f.write("{}\n".format(image_path))
    
    return text_path, total_file

text_path = write_image_path("store_data")