import os
from pathlib import Path
import pandas as pd


csv_file = 'train.csv'

def create_df():
    image_url = []
    folder_name=[]
    for file_path, folders, files in os.walk('dataset/train'):
        for file in files:
            full_path = os.path.join(file_path, file)
            if ".jpg" in full_path:
                image_url.append(full_path)
                direct = file_path.split('/')[2:]
                folder_name.append('/'.join(direct))

    data={
        'name': folder_name,
        'image_url': image_url,
    }

    df = pd.DataFrame(data, columns=['name','image_url'])
    return df


def create_csv(csv_file, df):
    file_path = Path(f'data/{csv_file}')
    if file_path.exists():
        df.to_csv(file_path, index=False, mode="a", header=False)    
        return f'The data is added to the <{csv_file}> file.'
    else:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(file_path, index=False, mode="w", header=True)
        return f'created <{csv_file}> file and data written to it'

print(create_csv(csv_file,create_df()))