import os
import sys
sys.path.insert(0, '/Users/namai/Documents/GitHub/Image')
import pandas as pd
from constants import train_dataset_path



def create_df(path_dir):
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

    df = pd.DataFrame(data, columns=['name','image_url'])
    df.to_csv('data/train.csv', index=False)
    return df
