import os
import sys
sys.path.insert(0, '/Users/namai/Documents/GitHub/Image/')
from constants import train_dataset_path, train_csv_file, apple_banana_csv_file
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2


def read_csv(csv_file):
    file_path = Path(f'data/{csv_file}')
    read_df = pd.read_csv(file_path)
    return read_df
# print(read_csv('train.csv'))


def create_dataset_df(path_dir):
    image_url = []
    folder_name=[]
    for file_path, folders, files in os.walk(path_dir):
        for file in files:
            full_path = os.path.join(file_path, file)
            if ".jpg" or '.jpeg' or '.png' or '.JPG' in full_path:
                image_url.append(full_path)
                direct = file_path.split('/')[8:]
                folder_name.append('/'.join(direct))
    data={
        'name': folder_name,
        'image_url': image_url,
    }
    
    dataset_df = pd.DataFrame(data, columns=['name','image_url'])
    dataset_df.to_csv('data/train.csv', index=False)
    return dataset_df


def resize_image(image_path, img_size): # img_size e.g. 122x122 tuple (122,122)
    """img_size 122x122 = e.g. (122,122)"""
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, img_size)
    img_rgb_array = np.array(img_resized)
    return img_rgb_array   


def resize_image_to_gray_lst(image_path, img_size):
    """img_size 122x122 = e.g. (122,122)"""
    img = plt.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_resized = cv2.resize(gray_img, img_size)  # White = [255,255,255], Black = [0,0,0], Gray=[122,122,122]
    img_gray_array = np.array(img_resized)
    image_gray_lst=[item for sublist in img_gray_array for item in sublist]
    return image_gray_lst   


def create_df_grey(csv_file, img_size):
    apple_banana = []
    img_lst = []
    line_path = read_csv(csv_file)['image_url']
  
    for line in range(len(line_path)):
        img_gray_lst = resize_image_to_gray_lst(line_path[line], img_size)
        img_lst.append(img_gray_lst)
        dir_name = line_path[line].split('/')[8:]
        apple_banana.append('/'.join(dir_name))
    
    img_data_df = pd.DataFrame(img_lst)
    apple_banana_df = pd.DataFrame(apple_banana, columns=['image_name'])
    df_grey = pd.concat([img_data_df, apple_banana_df], axis=1)
    df_grey.to_csv('data/grey_df.csv', index=False)
    return df_grey        
  


